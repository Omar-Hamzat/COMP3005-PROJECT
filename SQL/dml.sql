-- Insert entries into the members table
INSERT INTO members (username, password, address) VALUES
('James', '12345', '135 nepean'),
('julius', '54321', '305 overbrook');

-- Insert entries into the trainers table
INSERT INTO trainers (username, password, address) VALUES
('Jackson', '12345', '505 st-laurent'),
('Stacey', '3214', '341 orleans');

-- Insert entries into the admin table
INSERT INTO admin (username, password) VALUES
('Clarence', '12345'),
('John', '12345');

-- Insert entries into the equipment table
INSERT INTO equipment (name, functionality_status) VALUES
('Treadmill', true),
('Treadmill', true),
('Treadmill', false),
('Stationary Bike', false),
('Stationary Bike', false),
('Stationary Bike', false),
('Bench Press', true),
('Bench Press', false),
('Bench Press', true),
('Bench Press', true),
('Elliptical Trainer', true),
('Rowing Machine', false);
('Elliptical Trainer', true),
('Rowing Machine', false);

-- Insert entries into the trainer_payments table
INSERT INTO trainer_payments (trainer_id, paid) VALUES
(1, true),
(2, false);

-- Insert entries into the classes table
INSERT INTO classes (class_name, trainer_id, member_id, room_booked, date, time) VALUES
('Yoga', 1, 1, 'Room A', '2024-04-30', '10:00'),
('Zumba', 2, 2, 'Room B', '2024-05-01', '15:00');

-- Insert entries into the schedules table
INSERT INTO schedules (trainer_id, date, start_time, end_time, available) VALUES
(1, '2024-04-30', '08:00', '12:00', true),
(2, '2024-05-01', '13:00', '17:00', false);

-- Trainer 1 availability
INSERT INTO trainer_availability (trainer_id, day_of_week, start_time, end_time) VALUES
(1, 'Monday', '09:00:00', '17:00:00'),
(1, 'Tuesday', '10:00:00', '18:00:00'),
(1, 'Wednesday', '08:00:00', '16:00:00'),
(1, 'Thursday', '10:00:00', '18:00:00'),
(1, 'Friday', '09:00:00', '17:00:00');

-- Trainer 2 availability
INSERT INTO trainer_availability (trainer_id, day_of_week, start_time, end_time) VALUES
(2, 'Monday', '08:00:00', '16:00:00'),
(2, 'Tuesday', '09:00:00', '17:00:00'),
(2, 'Wednesday', '10:00:00', '18:00:00'),
(2, 'Thursday', '09:00:00', '17:00:00'),
(2, 'Friday', '08:00:00', '16:00:00');

-- Trainer 1 payroll profile
INSERT INTO payroll_profile (trainer_id, base_salary, bonus, deductions, total_pay) VALUES
(1, 3000, 500, 200, 3300);

-- Trainer 2 payroll profile
INSERT INTO payroll_profile (trainer_id, base_salary, bonus, deductions, total_pay) VALUES
(2, 3200, 600, 250, 3550);
