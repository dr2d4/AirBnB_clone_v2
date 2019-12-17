-- Make database dev
-- Create user develop
-- Give all the privileges
-- Give privileges to read the perfomance_schema
-- Restart privileges
CREATE DATABASE IF NOT EXISTS hbnb_dev_db CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

