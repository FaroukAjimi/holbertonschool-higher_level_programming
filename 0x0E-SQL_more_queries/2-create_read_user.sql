-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
DROP DATABASE 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
