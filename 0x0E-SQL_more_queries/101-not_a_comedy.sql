-- List TV show titles not associated with the 'Comedy' genre
USE hbtn_0d_tvshows;
SELECT ts.title
FROM tv_shows ts
WHERE ts.id NOT IN (
    SELECT ts.id
    FROM tv_shows ts
    JOIN tv_show_genres tsg ON ts.id = tsg.show_id
    JOIN tv_genres tg ON tsg.genre_id = tg.id
    WHERE tg.name = 'Comedy'
)
ORDER BY ts.title;
