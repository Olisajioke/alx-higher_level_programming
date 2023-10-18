-- List all genres and the number of shows linked to each from the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;
SELECT tv_genres.name AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
