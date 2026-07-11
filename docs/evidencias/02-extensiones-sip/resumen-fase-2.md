# Evidencia Fase 2 - Extensiones SIP

## Objetivo

Configurar extensiones SIP en Asterisk y validar llamadas internas para el sistema de confirmación automática de citas médicas.

## Extensiones configuradas

| Extensión | Uso | Estado |
|---|---|---|
| 1001 | Usuario de prueba 1 | Registrada |
| 1002 | Usuario de prueba 2 | Registrada |
| 2000 | Sistema automático de prueba | Funcional |
| 3000 | Reservada para AGI | Preparada |

## Pruebas realizadas

- Registro exitoso de extensión 1001.
- Registro exitoso de extensión 1002.
- Llamada interna 1001 hacia 1002.
- Llamada interna 1002 hacia 1001.
- Llamada hacia extensión 2000.
- Captura básica de DTMF en extensión 2000.

## Archivos configurados

- `/etc/asterisk/pjsip.conf`
- `/etc/asterisk/extensions.conf`
- `/etc/asterisk/rtp.conf`

## Observación de seguridad

La apertura de SIP/RTP hacia la PBX se realizó temporalmente solo desde la IP pública del administrador para pruebas iniciales. En la fase de SBC, la PBX será aislada del acceso público directo y aceptará tráfico únicamente desde el SBC.