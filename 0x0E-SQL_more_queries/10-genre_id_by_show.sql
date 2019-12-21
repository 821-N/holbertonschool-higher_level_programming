-- list each show and its genre id
SELECT show.title, genre.genre_id
FROM tv_shows show
INNER JOIN tv_show_genres genre
ON show.id = genre.show_id
ORDER BY show.title, genre.genre_id ASC;
