-- Lists all records of the table second_table having a name value in my MySQL server.
-- Records are ordered by score in descending.

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
