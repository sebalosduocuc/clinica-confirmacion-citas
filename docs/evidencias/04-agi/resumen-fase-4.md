\# Evidencia Fase 4 - Script AGI de Confirmación de Citas



\## Objetivo



Implementar un script AGI en Python que permita a Asterisk consultar citas pendientes, reproducir mensajes personalizados, capturar respuestas DTMF y actualizar la base de datos MariaDB.



\## Flujo validado



1\. La extensión 1001 llama a la extensión 3000.

2\. Asterisk ejecuta el script confirmar\_cita.py mediante AGI.

3\. El script identifica el número de origen mediante CALLERID(num).

4\. El script consulta la tabla citas en MariaDB.

5\. El sistema genera audio personalizado con datos de la cita.

6\. Se reproduce el mensaje al paciente.

7\. Se captura DTMF:

&#x20;  - 1 = confirmar

&#x20;  - 2 = cancelar

&#x20;  - 3 = reprogramar

8\. Se actualiza la tabla citas.

9\. Se registra trazabilidad en confirmaciones\_log.

10\. Se registra log técnico en /var/log/asterisk/confirmacion\_citas.log.



\## Resultado



La prueba con la extensión 1001 fue exitosa. La llamada hacia 3000 ejecutó el AGI, reprodujo audio personalizado, capturó la opción DTMF y actualizó correctamente el estado de la cita en la base de datos.



\## Archivos versionados



\- asterisk/agi-bin/confirmar\_cita.py

\- asterisk/agi-bin/agi\_db.example.conf

\- asterisk/extensions.conf

\- asterisk/pjsip.conf



\## Evidencias principales



\- Captura de ejecución del AGI.

\- Captura de audio personalizado sin error de archivo.

\- Captura DTMF 1 confirmada.

\- Captura DTMF 2 cancelada.

\- Captura DTMF 3 reprogramada.

\- Captura de tabla citas actualizada.

\- Captura de confirmaciones\_log.

\- Captura de log técnico AGI.

