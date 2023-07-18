-- Lists the number of records with the same score in the table second_table in my MySQL server.
-- Records are ordered by count in descending
-- The result display: the score, the number of records for this score with the label number
-- The database name will be passed as an argument to the mysql command

SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
