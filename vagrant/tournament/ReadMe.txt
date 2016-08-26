#Tournament utility:
###This program can be used as a back end utitily to track the players in a Swiss style tournament.


##Files included:
ReadMe.txt  --This file
**tournament.sql** --Used for setting up the SQL server
**tournament.py** --Main program file
**tournament_test.py** --used for testing the tournament.py file


##Dependencies:
The user must have a SQL server setup on their system before running this code.  
The code is setup to work with Psycopg2 but others can be substituted by changing the import on line 6 of tournament.py
NOTE: After changing SQL API please run tournament_test.py to ensure that everything still works.


##Setup:
In order to setup the SQL database either copy out the SQL commands from **tournament.sql** or run *\i tournament.sql* from the psql command line.


##Operation:
The **tournament.py** file has functions that can be called to support a tournament.  These are:

###*deleteMatches()*
Remove all the matches records from the database.

###*deletePlayers()*
Remove all the player records from the database.

###*countPlayers()*
Returns the number of players currently registered

###*registerPlayer(name)* 
Adds a player to the tournament database.

###*playerStandings()*
Returns a list of the players and their win records, sorted by wins. You can use the player standings table created in your .sql file for reference.

###*reportMatch(winner_id, loser_id)*
This is to simply populate the matches table and record the winner and loser as (winner,loser) in the insert statement.

###*swissPairings()*
Returns a list of pairs of players for the next round of a match. Here all we are doing is the pairing of alternate players from the player standings table, zipping them up and appending them to a list with values:
*(id1, name1, id2, name2)*



##Additional info about the program can be located [HERE](https://docs.google.com/document/d/1_QQ_FBcPROER-s674YT5WoV6wdpvGWZCI9b8_p0RJ_s/pub)