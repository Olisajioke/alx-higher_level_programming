-- List all cities in the hbtn_0d_usa database with their corresponding state names
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
