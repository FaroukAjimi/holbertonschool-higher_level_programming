-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT score,count(score) as number FROM second_table GROUP by score ORDER BY SCORE DESC;
