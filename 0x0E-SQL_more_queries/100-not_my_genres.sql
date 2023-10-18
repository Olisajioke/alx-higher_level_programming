-- List TV genre names not associated with "DEXTER"
USE hbtn_0d_tvshows;
SELECT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (
    SELECT tg.id
    FROM tv_genres tg
    JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
    JOIN tv_shows ts ON ts.id = tsg.show_id
    WHERE ts.title = "DEXTER"
)
ORDER BY tg.name;
