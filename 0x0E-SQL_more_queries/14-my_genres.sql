SELECT g.name -- get genres
FROM tv_genres g -- from list of genres
-- check that show name is "dexter"
INNER JOIN tv_show_genres t ON g.id = t.genre_id
INNER JOIN tv_shows s ON t.show_id = s.id
WHERE s.title = "Dexter"
--- sort
ORDER BY g.name ASC;
