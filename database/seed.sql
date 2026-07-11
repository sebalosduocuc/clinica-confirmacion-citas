USE clinica_citas;

INSERT INTO citas 
(codigo_paciente, nombre_paciente, telefono, especialidad, profesional, fecha_cita, hora_cita, estado)
VALUES
('PAC001', 'Felipe Silva', '1001', 'Medicina General', 'Dra. Carolina Rojas', '2026-07-20', '10:30:00', 'pendiente'),
('PAC002', 'Sebastian Lopez', '1002', 'Odontologia', 'Dr. Manuel Perez', '2026-07-20', '11:00:00', 'pendiente'),
('PAC003', 'Paciente Demo', '2000', 'Kinesiologia', 'Klgo. Andres Muñoz', '2026-07-21', '09:00:00', 'pendiente');
