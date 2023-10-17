-- Select the city and calculate the average temperature (in Fahrenheit)
SELECT city, AVG(value) AS avg_temperature
FROM temperatures
GROUP BY city
ORDER BY avg_temperature DESC;
