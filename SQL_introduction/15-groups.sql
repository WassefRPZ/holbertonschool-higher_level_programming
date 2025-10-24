-- that lists all databases of your MySQL server
SELECT score, count(id) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
