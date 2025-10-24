-- that lists all databases of your MySQL server
SELECT score, name
FROM second_table
WHERE name IS NOT null
ORDER BY score DESC;
