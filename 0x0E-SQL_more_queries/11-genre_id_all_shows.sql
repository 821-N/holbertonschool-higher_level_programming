-- list genres for all shows
SELECT show.title, genre.genre_id
FROM tv_shows show
LEFT JOIN tv_show_genres g
ON show.id = genre.show_id
ORDER BY show.title, genre.genre_id ASC;
