\# Evidencia Fase 8 - n8n, Slack y TTS externo



\## Objetivo



Implementar un flujo de automatización mediante n8n, integrando una API TTS dockerizada y envío de notificaciones hacia Slack.



\## Componentes implementados



\- VM independiente N8N-Docker-Clinica.

\- Docker Engine.

\- Docker Compose.

\- n8n.

\- API TTS en Flask.

\- espeak-ng para generación de audio.

\- Slack Incoming Webhook.

\- Workflow de confirmación de citas.



\## Flujo validado



1\. Se ejecuta workflow desde n8n.

2\. Un nodo Code genera datos de cita de prueba.

3\. n8n llama a la API TTS mediante HTTP Request.

4\. La API TTS genera un archivo de audio WAV.

5\. n8n envía un mensaje de confirmación a Slack.

6\. Slack recibe la notificación en el canal configurado.



\## Seguridad aplicada



\- n8n se expone solo desde la IP pública del administrador.

\- La API TTS no se expone directamente a Internet.

\- El webhook de Slack no se sube al repositorio.

\- Las credenciales reales quedan en archivo .env no versionado.

\- En ambiente de laboratorio se configuró N8N\_SECURE\_COOKIE=false para permitir acceso HTTP sin HTTPS.



\## Archivos versionados



\- docker-compose.yml

\- n8n/tts-api/app.py

\- n8n/tts-api/requirements.txt

\- n8n/tts-api/Dockerfile

\- n8n/.env.example

\- n8n/workflow-confirmacion-citas.json

