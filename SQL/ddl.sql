-- Table for members
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    address TEXT
);

-- Table for trainers
CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    address TEXT
);

-- Table for admin
CREATE TABLE admin (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Table for health metric
CREATE TABLE health_metrics (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    metric_name VARCHAR(255) NOT NULL,
    weight NUMERIC,
    height NUMERIC,
    pressure NUMERIC,
    rate NUMERIC
);


-- Table for equipment
CREATE TABLE equipment (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    functionality_status BOOLEAN NOT NULL
);

-- Table for trainer payment status
CREATE TABLE trainer_payments (
    id SERIAL PRIMARY KEY,
    trainer_id INTEGER NOT NULL,
    paid BOOLEAN NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES trainers (id)
);

-- Table for classes and room bookings
CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(255) NOT NULL,
    trainer_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    room_booked VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES trainers (id),
    FOREIGN KEY (member_id) REFERENCES members (id)
);

-- Table for schedules
CREATE TABLE schedules (
    id SERIAL PRIMARY KEY,
    trainer_id INTEGER NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    available BOOLEAN NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES trainers (id)
);

-- Table for training_sessions
CREATE TABLE training_sessions (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    trainer_id INT NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL
);
-- Table for fitness_goals
CREATE TABLE fitness_goals (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    target_weight NUMERIC,
    target_time VARCHAR(255) NOT NULL,
    cardio_records TEXT,
    weightlifting_goals TEXT
);

-- Table for trainer availability
CREATE TABLE trainer_availability (
    id SERIAL PRIMARY KEY,
    trainer_id INT NOT NULL,
    day_of_week VARCHAR(255) NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

-- Table for payroll_profile
CREATE TABLE payroll_profile (
    id SERIAL PRIMARY KEY,
    trainer_id INT NOT NULL,
    base_salary NUMERIC NOT NULL,
    bonus NUMERIC,
    deductions NUMERIC,
    total_pay NUMERIC
);


