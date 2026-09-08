CREATE DATABASE alpacino_db;
USE alpacino_db;
CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    type VARCHAR(50),
    country_origin VARCHAR(100),
    director VARCHAR(255),
    languages VARCHAR(255),
    plot TEXT,
    metascore INT,
    genre VARCHAR(255),
    rating DECIMAL(3,1),
    release_date DATE
);
SELECT * FROM movies;