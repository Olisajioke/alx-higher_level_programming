-- List all shows in the hbtn_0d_tvshows database with their associated genre IDs (or NULL if no genre)
USE hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
