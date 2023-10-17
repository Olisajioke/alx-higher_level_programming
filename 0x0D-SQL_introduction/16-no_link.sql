-- List records from the second_table with a name value, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
