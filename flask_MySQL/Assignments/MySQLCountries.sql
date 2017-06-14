use World;
/*
SELECT * 
FROM COUNTRIES;

SELECT * 
FROM cities;

SELECT cou
FROM countries
JOIN cities ON countries.id = cities.country_id;

SELECT c.name, l.language, l.percentage
FROM countries as c
JOIN languages as l
ON c.id = l.country_id
WHERE language = 'Slovene'
ORDER BY l.percentage DESC;
*/
/*
2. 
SELECT c.name, count(ct.name) as CityCount
FROM countries as c 
JOIN cities as ct
ON c.id = ct.country_id
GROUP BY c.name;
*/

-- 3 
/*
SELECT ct.name, ct.population, c.name
FROM countries as c 
JOIN cities as ct
ON c.id = ct.country_id
WHERE ct.country_id = 136 and ct.population > 500000
ORDER BY ct.population DESC;
*/
-- 4 

SELECT l.language, c.name as Country_Name, l.percentage
FROM countries as c
JOIN languages as l
ON c.id = l.country_id
WHERE l.percentage > 89
ORDER BY l.percentage DESC;

-- 5 

