\# Evidencia Fase 7 - Implementación de SIP/TLS en SBC Kamailio



\## Objetivo



Implementar señalización SIP cifrada mediante TLS en el SBC Kamailio, permitiendo que el cliente SIP se conecte al SBC por TCP 5061.



\## Flujo implementado



1\. MicroSIP se configura con transporte TLS.

2\. El cliente se conecta al SBC por TCP 5061.

3\. Kamailio recibe la señalización cifrada.

4\. El SBC termina TLS y reenvía internamente hacia la PBX por UDP 5060.

5\. La PBX autentica la extensión 1001.

6\. La llamada a 3000 llega a Asterisk.

7\. Asterisk ejecuta el script AGI.

8\. El usuario responde con DTMF.

9\. MariaDB actualiza el estado de la cita.



\## Componentes utilizados



\- Kamailio

\- Módulo tls.so

\- OpenSSL

\- Certificado autofirmado de laboratorio

\- MicroSIP con transporte TLS

\- Asterisk PJSIP

\- MariaDB

\- tcpdump

\- sngrep



\## Seguridad aplicada



\- La señalización desde el cliente hacia el SBC se cifra mediante TLS.

\- El puerto TCP 5061 se habilita únicamente desde la IP del administrador.

\- La PBX se mantiene aislada y solo recibe SIP/RTP desde el Security Group del SBC.

\- La clave privada TLS no se sube al repositorio.



\## Evidencias principales



\- Certificado TLS generado.

\- Archivo tls.cfg configurado.

\- Kamailio escuchando en TCP 5061.

\- Prueba OpenSSL contra el puerto 5061.

\- MicroSIP registrado mediante TLS.

\- Captura tcpdump de tráfico TCP 5061.

\- Llamada hacia 3000 usando TLS.

\- Ejecución AGI.

\- Actualización de cita en MariaDB.

