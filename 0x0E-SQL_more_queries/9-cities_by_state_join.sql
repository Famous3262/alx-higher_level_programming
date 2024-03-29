-- lists all cities contained in the database hbtn_0d_usa.
-- Each record displays: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id
-- The database name is passed as an argument of the mysql command

SELECT cities.id, cities.name, states.name FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
