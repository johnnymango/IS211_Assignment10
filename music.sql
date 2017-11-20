-- IS211 Assignment 10


-- Deletes Tables if they exist
DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS songs;


-- Creates the artists table
CREATE TABLE artists 
(
	artist_id int PRIMARY KEY, 
	artist_name TEXT
);

-- Creates albums table
CREATE TABLE albums 
(
	album_id int PRIMARY KEY, 
	album_name text,	
        artist_id int
);

-- Creates songs table
CREATE TABLE songs 
(
	song_id int PRIMARY KEY, 
	song_name text,
	artist_id int,
        album_id int, 
	track_number int, 
	song_length int
);
