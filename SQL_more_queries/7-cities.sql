-- that lists all privileges of the
-- MySQL users user_0d_1 and user_0d_2
CREATE DATABASE if NOT EXISTS hbtn_0d_usa;
CREATE TABLE if NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
