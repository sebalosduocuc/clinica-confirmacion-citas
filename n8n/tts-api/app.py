from flask import Flask, request, jsonify, send_from_directory
import os
import re
import time
import subprocess

app = Flask(__name__)

AUDIO_DIR = "/app/audios"
os.makedirs(AUDIO_DIR, exist_ok=True)

def limpiar_nombre(nombre: str) -> str:
    nombre = nombre.lower().strip()
    nombre = re.sub(r"[^a-z0-9_-]+", "_", nombre)
    return nombre[:60] or f"audio_{int(time.time())}"

@app.get("/health")
def health():
    return jsonify({
        "ok": True,
        "servicio": "tts-api-clinica",
        "estado": "operativo"
    })

@app.post("/tts")
def generar_tts():
    data = request.get_json(silent=True) or {}
    texto = data.get("texto", "").strip()
    nombre = data.get("nombre", f"audio_{int(time.time())}")

    if not texto:
        return jsonify({
            "ok": False,
            "error": "Debe enviar el campo texto"
        }), 400

    nombre_limpio = limpiar_nombre(nombre)
    archivo = f"{nombre_limpio}.wav"
    ruta = os.path.join(AUDIO_DIR, archivo)

    try:
        subprocess.run(
            ["espeak-ng", "-v", "es", "-s", "145", "-w", ruta, texto],
            check=True
        )

        return jsonify({
            "ok": True,
            "archivo": archivo,
            "ruta": ruta,
            "texto": texto
        })

    except subprocess.CalledProcessError as e:
        return jsonify({
            "ok": False,
            "error": "No se pudo generar audio TTS",
            "detalle": str(e)
        }), 500

@app.get("/audios/<path:filename>")
def audios(filename):
    return send_from_directory(AUDIO_DIR, filename)
