CREATE DATABASE netflix_db;
USE netflix_db;

CREATE TABLE netflix_titles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(20),
    title VARCHAR(255),
    director VARCHAR(255),
    cast_members TEXT,
    country VARCHAR(255),
    date_added VARCHAR(100),
    release_year INT,
    rating VARCHAR(20),
    duration VARCHAR(50),
    listed_in VARCHAR(255)
);

SELECT COUNT(*) AS total_records
FROM netflix_titles;

SELECT type, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY type;

SELECT country, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;

SELECT director, COUNT(*) AS total_titles
FROM netflix_titles
WHERE director <> 'UNKNOWN'
GROUP BY director
ORDER BY total_titles DESC
LIMIT 10;

SELECT rating, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY rating
ORDER BY total_titles DESC;

SELECT release_year, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year
ORDER BY release_year DESC;

SELECT listed_in, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY listed_in
ORDER BY total_titles DESC
LIMIT 10;

SELECT *
FROM netflix_titles
WHERE country LIKE '%India%';

SELECT *
FROM netflix_titles
WHERE release_year >= 2020;

CREATE VIEW netflix_summary AS
SELECT
    title,
    type,
    country,
    release_year,
    rating
FROM netflix_titles;

DELIMITER $$

CREATE PROCEDURE GetContentByYear(IN p_year INT)
BEGIN
    SELECT *
    FROM netflix_titles
    WHERE release_year = p_year;
END $$

DELIMITER ;

CALL GetContentByYear(2021);