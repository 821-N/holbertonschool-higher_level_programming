-- list cities and their states
SELECT city.id, city.name, state.name
FROM cities city
LEFT JOIN states state
ON city.state_id = state.id
ORDER BY city.id ASC;
