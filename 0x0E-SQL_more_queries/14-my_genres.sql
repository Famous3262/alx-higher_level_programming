-- lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id is different)
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name
-- The database name is passed as an argument of the mysql command

SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;
