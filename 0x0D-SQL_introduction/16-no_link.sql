-- print number of users that have each score
SELECT score, name
FROM second_table
WHERE (name IS NOT NULL)
ORDER BY score DESC;
