-- that lists all privileges of the
-- MySQL users user_0d_1 and user_0d_2
CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
CREATE TABLE if NOT EXISTS hbtn_0d_usa.states (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
