-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
ALTER DATABASE
hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8m4_unicode_ci;
ALTER TABLE
first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
ALTER TABLE
first_name
CHANGE name
VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
