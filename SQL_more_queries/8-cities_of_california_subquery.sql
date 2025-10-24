-- that lists all privileges of the
-- MySQL users user_0d_1 and user_0d_2
SELECT cities.id, cities.name
FROM states, cities
WHERE states.id = cities.state_id AND states.name = 'California'
ORDER BY cities.id;
