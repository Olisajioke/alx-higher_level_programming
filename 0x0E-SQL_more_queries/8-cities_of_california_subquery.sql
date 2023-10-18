-- List all the cities of California from the hbtn_0d_usa database
USE hbtn_0d_usa;
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id;
