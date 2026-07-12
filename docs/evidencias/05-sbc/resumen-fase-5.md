\# Evidencia Fase 5 - Despliegue de SBC Kamailio



\## Objetivo



Desplegar un SBC open source en una VM independiente dentro de AWS y comenzar el aislamiento de la PBX Asterisk del acceso público directo.



\## Instancia SBC



\- Nombre: SBC-Kamailio-Clinica

\- Sistema operativo: Ubuntu Server

\- Software SBC: Kamailio

\- Herramientas: sngrep, net-tools, curl, nano, git



\## Función del SBC



El SBC actúa como punto de entrada controlado para el tráfico SIP/RTP. La PBX Asterisk deja de exponerse directamente a Internet para tráfico SIP y RTP. En fases posteriores, Kamailio se configurará para enrutar tráfico hacia la PBX y posteriormente se incorporará TLS.



\## Seguridad aplicada



\- El SBC queda expuesto solo desde la IP del administrador para pruebas iniciales.

\- La PBX mantiene SSH únicamente desde la IP del administrador.

\- La PBX acepta SIP/RTP solo desde el Security Group del SBC.

\- Se elimina el acceso SIP/RTP directo desde clientes hacia la PBX.



\## Evidencias principales



\- Instancia EC2 SBC creada.

\- IP pública y privada del SBC.

\- Kamailio instalado.

\- Servicio Kamailio activo.

\- Puerto 5060 escuchando.

\- Security Group del SBC.

\- Security Group de la PBX restringido solo al SBC.

\- Conectividad privada SBC hacia PBX.

