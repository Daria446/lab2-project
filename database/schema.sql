PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS adoptions;
DROP TABLE IF EXISTS adopters;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    position TEXT NOT NULL,
    phone TEXT
);

CREATE TABLE animals (
    animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    age INTEGER,
    health_status TEXT NOT NULL DEFAULT 'Не указан',
    arrival_date TEXT NOT NULL
);

CREATE TABLE adopters (
    adopter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    address TEXT
);

CREATE TABLE adoptions (
    adoption_id INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_id INTEGER NOT NULL UNIQUE,
    adopter_id INTEGER NOT NULL,
    employee_id INTEGER NOT NULL,
    adoption_date TEXT NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES animals(animal_id),
    FOREIGN KEY (adopter_id) REFERENCES adopters(adopter_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO employees (full_name, position, phone) VALUES
('Анна Иванова', 'Администратор', '+70000000001'),
('Иван Петров', 'Ветеринар', '+70000000002'),
('Мария Смирнова', 'Сотрудник приюта', '+70000000003');

INSERT INTO animals (name, species, age, health_status, arrival_date) VALUES
('Барсик', 'Кошка', 2, 'Здоров', '2026-10-01'),
('Рекс', 'Собака', 4, 'Требует осмотра', '2026-10-03'),
('Мурка', 'Кошка', 1, 'Здорова', '2026-10-05'),
('Дружок', 'Собака', 3, 'Здоров', '2026-10-08');

INSERT INTO adopters (full_name, phone, address) VALUES
('Елена Соколова', '+70000000011', 'Нижний Новгород'),
('Дмитрий Козлов', '+70000000012', 'Нижний Новгород'),
('Ольга Васильева', '+70000000013', 'Кстово');

INSERT INTO adoptions (animal_id, adopter_id, employee_id, adoption_date) VALUES
(1, 1, 1, '2026-10-10'),
(3, 2, 3, '2026-10-12');