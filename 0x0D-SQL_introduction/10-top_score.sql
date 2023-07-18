-- Lists all records of the table second_table.
-- Records are ordered by descending score.
-- The database name will be passed as an argument of the mysql command
-- Results display both the score and the name

SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
