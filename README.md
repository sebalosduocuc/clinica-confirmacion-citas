<<<<<<< HEAD
\# Sistema Automatizado de Confirmación de Citas Médicas



\## Caso de estudio



La Clínica Regional "Salud Integral" requiere modernizar su proceso de confirmación de citas médicas, debido al alto porcentaje de ausencias de pacientes y al uso de llamadas manuales realizadas por personal administrativo.



Este proyecto implementa una solución basada en comunicaciones unificadas, compuesta por una central telefónica IP, un SBC para seguridad perimetral, señalización SIP cifrada mediante TLS, un flujo de automatización en n8n, integración con Slack, servicio TTS y una base de datos de citas.



\## Objetivo general



Diseñar, implementar y desplegar un sistema automatizado de confirmación de citas médicas, capaz de realizar llamadas, reproducir mensajes personalizados, capturar respuestas DTMF y actualizar el estado de las citas en una base de datos.



\## Objetivos específicos



\- Desplegar una central telefónica IP basada en Asterisk.

\- Configurar extensiones SIP para pruebas de llamadas.

\- Implementar un script AGI para el flujo de confirmación de citas.

\- Consultar y actualizar una base de datos de citas médicas.

\- Implementar un SBC para proteger la PBX del acceso público directo.

\- Configurar transporte SIP sobre TLS.

\- Validar la seguridad mediante herramientas de análisis de tráfico.

\- Integrar n8n con Slack, IA y TTS.

\- Documentar la solución técnica y sus evidencias.



\## Componentes principales



\- Asterisk PBX

\- Extensiones SIP

\- Script AGI en Python

\- Base de datos MariaDB

\- SBC open source

\- SIP sobre TLS

\- n8n

\- Slack API

\- Servicio TTS

\- Docker

\- Herramientas de análisis de tráfico



\## Estructura del repositorio



\- `/asterisk`: archivos de configuración de la PBX.

\- `/database`: scripts SQL de la base de datos.

\- `/sbc`: configuración del SBC.

\- `/n8n`: exportación del flujo n8n.

\- `/scripts`: scripts auxiliares.

\- `/docs`: arquitectura, evidencias e informe.

\- `/logs`: ejemplos de logs generados por el sistema.



\## Estado del proyecto



En desarrollo.

=======
# clinica-confirmacion-citas
Sistema automatizado de confirmación de citas médicas con Asterisk, SBC, n8n y TTS
>>>>>>> 67ec75a0a6e39850014251f29c09a9cc74093221
