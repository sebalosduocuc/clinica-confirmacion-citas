CREATE DATABASE IF NOT EXISTS clinica_citas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE clinica_citas;

CREATE TABLE IF NOT EXISTS citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_paciente VARCHAR(20) NOT NULL,
    nombre_paciente VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    profesional VARCHAR(100) NOT NULL,
    fecha_cita DATE NOT NULL,
    hora_cita TIME NOT NULL,
    estado VARCHAR(30) NOT NULL DEFAULT 'pendiente',
    respuesta_dtmf VARCHAR(10) DEFAULT NULL,
    intentos INT NOT NULL DEFAULT 0,
    ultima_respuesta DATETIME DEFAULT NULL,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS confirmaciones_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cita_id INT NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    opcion_dtmf VARCHAR(10),
    resultado VARCHAR(50) NOT NULL,
    detalle VARCHAR(255),
    fecha_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cita_id) REFERENCES citas(id)
);
