-- List TV show titles and their associated genre names
USE hbtn_0d_tvshows;
SELECT title, name
FROM tv_shows
LEFT JOIN tv_show_genres ON id = show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name;
