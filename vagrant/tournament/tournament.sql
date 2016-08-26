
-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--clears any previous database if needed
\c vagrant
DROP DATABASE tournament;

-- Create the database
CREATE DATABASE tournament;

--Move into database
\c tournament

--Create players table
CREATE TABLE players (
	id serial primary key,
	name text
	);

--Create matches table
CREATE TABLE matches (
	id serial primary key,
	winner integer references players(id),
	loser integer references players(id)
	);

CREATE VIEW standings AS 
	SELECT players.id, players.name, 
	(SELECT count(*) from matches where players.id = matches.winner) as wins,
	(SELECT count(*) from matches where players.id = matches.winner or players.id = matches.loser) as matches
	from players left join matches 
	ON players.id = matches.winner 
	GROUP BY players.id order by wins desc