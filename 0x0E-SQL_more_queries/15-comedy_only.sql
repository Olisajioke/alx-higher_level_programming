-- List TV show titles in the 'Comedy' genre
USE hbtn_0d_tvshows;
SELECT title
FROM tv_shows
JOIN tv_show_genres ON id = show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
