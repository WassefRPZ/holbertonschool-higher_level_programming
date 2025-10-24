SELECT cities.id, cities.name
FROM states, cities
WHERE states.id = cities.state_id AND states.name = 'California'
ORDER BY cities.id;