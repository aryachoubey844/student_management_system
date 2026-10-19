CREATE DATABASE student_db;
USE student_db;
CREATE TABLE users (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50));
CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT, course VARCHAR(50), marks INT);
INSERT INTO users VALUES ('admin', 'admin123');