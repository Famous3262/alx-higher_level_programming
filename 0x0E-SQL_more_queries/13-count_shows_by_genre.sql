-- Lists all genres from the database hbtn_0d_tvshows
-- and display the number of shows linked to each.
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column is called "genre"
-- Second column is called "number_of_shows"
-- Results are sorted in descending order by the number of shows linked
-- The database name is passed as an argument of the mysql command

SELECT tv_genres.name AS 'genre', COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
