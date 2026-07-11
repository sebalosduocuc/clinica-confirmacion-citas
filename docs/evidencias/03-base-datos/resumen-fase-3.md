\# Evidencia Fase 3 - Base de Datos de Citas



\## Objetivo



Crear una base de datos MariaDB para almacenar citas médicas, estados de confirmación y trazabilidad de respuestas DTMF.



\## Base de datos creada



\- Nombre: clinica\_citas

\- Motor: MariaDB

\- Codificación: utf8mb4



\## Tablas creadas



\### citas



Tabla principal donde se almacenan los datos de las citas médicas:

\- Código de paciente

\- Nombre del paciente

\- Teléfono o extensión de contacto

\- Especialidad

\- Profesional

\- Fecha y hora de cita

\- Estado

\- Respuesta DTMF

\- Intentos

\- Fecha de última respuesta



\### confirmaciones\_log



Tabla de trazabilidad para registrar cada intento de confirmación:

\- Cita asociada

\- Teléfono

\- Opción DTMF

\- Resultado

\- Detalle

\- Fecha del evento



\## Estados considerados



\- pendiente

\- confirmada

\- cancelada

\- reprogramar

\- sin\_respuesta

\- error



\## Pruebas realizadas



\- Creación de base de datos.

\- Creación de usuario de aplicación.

\- Creación de tabla citas.

\- Creación de tabla confirmaciones\_log.

\- Inserción de registros de prueba.

\- Actualización manual de estado.

\- Registro de evento en tabla confirmaciones\_log.



\## Archivos asociados



\- database/schema.sql

\- database/seed.sql

