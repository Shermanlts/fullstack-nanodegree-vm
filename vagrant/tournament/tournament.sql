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

--Create Standings table
--Opponent match wins is omw
CREATE TABLE standings (
	id serial references players,
	rank integer,
	wins integer,
	losses integer,
	omw integer
	);

--Create matches table
CREATE TABLE matches (
	id serial primary key,
	winner integer references players,
	loser integer references players,
	round integer
	);
