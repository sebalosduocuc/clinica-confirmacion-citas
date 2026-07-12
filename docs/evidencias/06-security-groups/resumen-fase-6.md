\# Evidencia Fase 6 - Enrutamiento SBC Kamailio hacia PBX Asterisk



\## Objetivo



Configurar reglas de enrutamiento en Kamailio para permitir que los clientes SIP se registren y realicen llamadas hacia la PBX Asterisk pasando por el SBC.



\## Flujo implementado



1\. Cliente SIP se registra contra la IP pública del SBC.

2\. Kamailio recibe el REGISTER en UDP 5060.

3\. Kamailio reenvía el tráfico SIP hacia la PBX Asterisk por IP privada.

4\. La PBX autentica la extensión SIP.

5\. El cliente llama a la extensión 3000.

6\. La llamada pasa por Kamailio y llega a Asterisk.

7\. Asterisk ejecuta el AGI de confirmación de citas.

8\. El usuario presiona DTMF.

9\. La base de datos MariaDB actualiza el estado de la cita.



\## Componentes usados



\- SBC: Kamailio

\- Relay RTP: RTPengine

\- PBX: Asterisk

\- Base de datos: MariaDB

\- Cliente SIP: MicroSIP

\- Herramienta de análisis: sngrep



\## Seguridad aplicada



\- La PBX no recibe SIP/RTP directamente desde Internet.

\- El SBC actúa como punto de entrada controlado.

\- La PBX acepta tráfico SIP/RTP únicamente desde el Security Group del SBC.

\- La administración SSH se mantiene restringida a la IP del administrador.



\## Archivos versionados



\- sbc/kamailio.cfg

\- sbc/rtpengine-clinica.service

\- asterisk/pjsip.conf



\## Evidencias principales



\- Registro de MicroSIP vía SBC.

\- Captura sngrep de tráfico SIP.

\- Contacto PJSIP registrado en PBX.

\- Llamada hacia extensión 3000 pasando por SBC.

\- Ejecución del AGI.

\- Actualización de cita en base de datos.

\- Logs de Kamailio.

