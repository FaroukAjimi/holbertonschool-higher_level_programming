-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
id INT NOT NULL AUTO_INCREMENT,
UNIQUE KEY (id),
name VARCHAR(256) NOT NULL);
