\# Evidencia Fase 9 - Cierre final y pruebas integradas



\## Objetivo



Validar el funcionamiento completo del sistema automatizado de confirmación de citas médicas y preparar la entrega final del proyecto.



\## Componentes validados



\- PBX Asterisk.

\- Base de datos MariaDB.

\- Script AGI confirmar\_cita.py.

\- SBC Kamailio.

\- RTPengine.

\- SIP/TLS en puerto TCP 5061.

\- n8n en Docker.

\- API TTS dockerizada.

\- Slack Incoming Webhook.

\- Repositorio GitHub.

\- Informe técnico final.



\## Prueba integrada principal



Se validó el flujo:



MicroSIP TLS -> SBC Kamailio -> PBX Asterisk -> AGI -> MariaDB



Resultado:



\- El cliente SIP se registró mediante SBC.

\- La llamada hacia la extensión 3000 llegó a Asterisk.

\- Asterisk ejecutó el script AGI.

\- El sistema reprodujo audio personalizado.

\- Se capturó respuesta DTMF.

\- MariaDB actualizó el estado de la cita.

\- Se registró trazabilidad en confirmaciones\_log.



\## Prueba de automatización



Se validó el flujo:



n8n -> API TTS -> Slack



Resultado:



\- n8n ejecutó el workflow.

\- El nodo Code generó datos de cita.

\- El nodo HTTP Request llamó a la API TTS.

\- La API TTS generó audio WAV.

\- n8n envió notificación a Slack.

\- Slack recibió el mensaje correctamente.



\## Seguridad revisada



\- PBX aislada para SIP/RTP mediante Security Groups.

\- SBC como punto de entrada controlado.

\- SIP/TLS habilitado hacia el SBC.

\- n8n expuesto solo desde la IP del administrador.

\- API TTS no expuesta directamente a Internet.

\- Webhook de Slack no versionado.

\- Archivo .env no versionado.



\## Estado final



La solución queda funcional y documentada para entrega final.

