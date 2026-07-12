#!/usr/bin/env python3
import sys
import os
import re
import time
import logging
import tempfile
import subprocess
import configparser
from datetime import date, time as dt_time

import pymysql
import pymysql.cursors


LOG_FILE = "/var/log/asterisk/confirmacion_citas.log"
DB_CONFIG_FILE = "/etc/asterisk/agi_db.conf"
SOUNDS_DIR = "/usr/share/asterisk/sounds/en_US_f_Allison"
CUSTOM_SOUND_PREFIX = "custom/citas"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def leer_agi_env():
    env = {}
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            env[key.strip()] = value.strip()
    return env


def agi_cmd(command):
    sys.stdout.write(command + "\n")
    sys.stdout.flush()
    response = sys.stdin.readline().strip()
    logging.info("AGI CMD: %s | RESPONSE: %s", command, response)
    return response


def agi_verbose(message, level=1):
    safe = message.replace('"', "'")
    agi_cmd(f'VERBOSE "{safe}" {level}')


def parse_agi_result(response):
    match = re.search(r"result=([0-9-]+)", response)
    if not match:
        return ""
    result = match.group(1)

    # Algunas respuestas AGI pueden devolver ASCII en vez del dígito.
    ascii_map = {
        "49": "1",
        "50": "2",
        "51": "3"
    }

    return ascii_map.get(result, result)


def limpiar_telefono(value):
    if not value:
        return ""
    return re.sub(r"[^0-9]", "", value)


def leer_config_db():
    config = configparser.ConfigParser()
    read_files = config.read(DB_CONFIG_FILE)

    if not read_files:
        raise RuntimeError(f"No se pudo leer el archivo de configuración {DB_CONFIG_FILE}")

    return {
        "host": config.get("database", "host"),
        "user": config.get("database", "user"),
        "password": config.get("database", "password"),
        "database": config.get("database", "database"),
        "cursorclass": pymysql.cursors.DictCursor,
        "charset": "utf8mb4",
        "autocommit": False
    }


def conectar_db():
    db_config = leer_config_db()
    return pymysql.connect(**db_config)


def formatear_fecha(valor):
    if isinstance(valor, date):
        return valor.strftime("%d-%m-%Y")
    return str(valor)


def formatear_hora(valor):
    if isinstance(valor, dt_time):
        return valor.strftime("%H:%M")
    return str(valor)


def generar_audio_tts(texto, nombre_archivo):
    """
    Genera audio WAV compatible con Asterisk:
    8000 Hz, mono, 16 bits.
    Retorna la ruta relativa sin extensión para usar en STREAM FILE.
    """

    nombre_limpio = re.sub(r"[^a-zA-Z0-9_]", "_", nombre_archivo)
    archivo_tmp = os.path.join(tempfile.gettempdir(), f"{nombre_limpio}_tmp.wav")

    ruta_relativa = f"{CUSTOM_SOUND_PREFIX}/{nombre_limpio}"
    archivo_final = os.path.join(SOUNDS_DIR, f"{ruta_relativa}.gsm")

    subprocess.run(
        ["espeak-ng", "-v", "es", "-s", "145", "-w", archivo_tmp, texto],
        check=True
    )
    
    subprocess.run(
    [
        "sox",
        archivo_tmp,
        "-r", "8000",
        "-c", "1",
        archivo_final
    ],
    check=True
) 
 
    try:
        os.remove(archivo_tmp)
    except OSError:
        pass

    return ruta_relativa


def reproducir_texto(texto, nombre_archivo):
    try:
        sound_key = generar_audio_tts(texto, nombre_archivo)
        agi_cmd(f'STREAM FILE {sound_key} ""')
    except Exception as error:
        logging.exception("Error generando/reproduciendo audio TTS: %s", error)
        agi_cmd('STREAM FILE hello-world ""')


def buscar_cita_pendiente(connection, telefono):
    with connection.cursor() as cursor:
        sql = """
            SELECT id, codigo_paciente, nombre_paciente, telefono, especialidad,
                   profesional, fecha_cita, hora_cita, estado
            FROM citas
            WHERE telefono = %s
              AND estado = 'pendiente'
            ORDER BY fecha_cita ASC, hora_cita ASC
            LIMIT 1
        """
        cursor.execute(sql, (telefono,))
        return cursor.fetchone()


def actualizar_cita(connection, cita_id, telefono, opcion):
    if opcion == "1":
        nuevo_estado = "confirmada"
        resultado = "confirmada"
        detalle = "Paciente confirmó asistencia mediante DTMF 1."
    elif opcion == "2":
        nuevo_estado = "cancelada"
        resultado = "cancelada"
        detalle = "Paciente canceló la cita mediante DTMF 2."
    elif opcion == "3":
        nuevo_estado = "reprogramar"
        resultado = "reprogramar"
        detalle = "Paciente solicitó reprogramación mediante DTMF 3."
    else:
        nuevo_estado = "sin_respuesta"
        resultado = "sin_respuesta"
        detalle = "No se recibió una opción DTMF válida."

    with connection.cursor() as cursor:
        sql_update = """
            UPDATE citas
            SET estado = %s,
                respuesta_dtmf = %s,
                intentos = intentos + 1,
                ultima_respuesta = NOW()
            WHERE id = %s
        """
        cursor.execute(sql_update, (nuevo_estado, opcion if opcion else None, cita_id))

        sql_log = """
            INSERT INTO confirmaciones_log
            (cita_id, telefono, opcion_dtmf, resultado, detalle)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_log, (cita_id, telefono, opcion if opcion else None, resultado, detalle))

    connection.commit()
    return nuevo_estado, resultado, detalle


def main():
    agi_env = leer_agi_env()

    caller_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    caller_id = caller_arg or agi_env.get("agi_callerid", "")
    telefono = limpiar_telefono(caller_id)

    logging.info("Inicio AGI confirmar_cita.py | caller_id=%s | telefono=%s", caller_id, telefono)

    agi_cmd("ANSWER")
    agi_verbose("AGI de confirmación de citas iniciado", 1)

    if not telefono:
        reproducir_texto(
            "No fue posible identificar el número de origen de la llamada.",
            f"error_sin_telefono_{int(time.time())}"
        )
        agi_cmd("HANGUP")
        return

    try:
        connection = conectar_db()
    except Exception as error:
        logging.exception("Error conectando a base de datos: %s", error)
        reproducir_texto(
            "El sistema no pudo conectarse a la base de datos de citas.",
            f"error_db_{int(time.time())}"
        )
        agi_cmd("HANGUP")
        return

    try:
        cita = buscar_cita_pendiente(connection, telefono)

        if not cita:
            logging.info("No se encontró cita pendiente para telefono=%s", telefono)
            reproducir_texto(
                "No se encontró una cita pendiente asociada a este número.",
                f"sin_cita_{telefono}_{int(time.time())}"
            )
            agi_cmd("HANGUP")
            return

        cita_id = cita["id"]
        nombre = cita["nombre_paciente"]
        especialidad = cita["especialidad"]
        profesional = cita["profesional"]
        fecha = formatear_fecha(cita["fecha_cita"])
        hora = formatear_hora(cita["hora_cita"])

        mensaje = (
            f"Hola {nombre}. "
            f"Le recordamos su cita de {especialidad} con {profesional}, "
            f"programada para el día {fecha} a las {hora}. "
            f"Para confirmar su asistencia, presione 1. "
            f"Para cancelar la cita, presione 2. "
            f"Para solicitar reprogramación, presione 3."
        )

        reproducir_texto(mensaje, f"cita_{cita_id}_{int(time.time())}")

        respuesta = agi_cmd("GET DATA beep 10000 1")
        opcion = parse_agi_result(respuesta)

        logging.info("Cita ID=%s | telefono=%s | opcion DTMF=%s", cita_id, telefono, opcion)

        nuevo_estado, resultado, detalle = actualizar_cita(connection, cita_id, telefono, opcion)

        if nuevo_estado == "confirmada":
            respuesta_audio = "Su cita ha sido confirmada correctamente. Muchas gracias."
        elif nuevo_estado == "cancelada":
            respuesta_audio = "Su cita ha sido cancelada. Muchas gracias por informar."
        elif nuevo_estado == "reprogramar":
            respuesta_audio = "Su solicitud de reprogramación fue registrada. La clínica se comunicará con usted."
        else:
            respuesta_audio = "No se recibió una opción válida. La clínica podrá contactarse nuevamente."

        reproducir_texto(respuesta_audio, f"resultado_{cita_id}_{int(time.time())}")

        logging.info(
            "Resultado AGI | cita_id=%s | telefono=%s | estado=%s | detalle=%s",
            cita_id,
            telefono,
            nuevo_estado,
            detalle
        )

    except Exception as error:
        logging.exception("Error general en AGI: %s", error)
        try:
            connection.rollback()
        except Exception:
            pass

        reproducir_texto(
            "Ocurrió un error procesando la confirmación de su cita.",
            f"error_general_{int(time.time())}"
        )

    finally:
        try:
            connection.close()
        except Exception:
            pass

        agi_cmd("HANGUP")


if __name__ == "__main__":
    main()
