CREATE DATABASE ems_pro;

USE ems_pro;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(20) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    department VARCHAR(50),
    job_title VARCHAR(50),
    salary DECIMAL(10,2),
    date_joined DATE,
    status VARCHAR(20) DEFAULT 'Active'
);
