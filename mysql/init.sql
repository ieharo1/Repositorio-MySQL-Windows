CREATE DATABASE IF NOT EXISTS salesdb;

CREATE USER IF NOT EXISTS 'sales'@'%' IDENTIFIED BY 'salespass';
GRANT ALL PRIVILEGES ON salesdb.* TO 'sales'@'%';
FLUSH PRIVILEGES;

USE salesdb;

CREATE TABLE IF NOT EXISTS sales (
  id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id VARCHAR(32),
  product VARCHAR(64),
  region VARCHAR(32),
  quantity INT,
  price DECIMAL(10,2),
  sold_at DATETIME
);

