/*  */
CREATE database IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT all ON hbnb_dev_db to hbnb_dev'@'localhost;
GRANT SELECT ON hbnb_dev_db to hbnb_dev'@'localhost;

