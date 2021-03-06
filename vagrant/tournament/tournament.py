#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except:
        print("Connection failed")


def deleteMatches():
    """Remove all the match records from the database."""
    DB= connect()
    c = DB.cursor()
    c.execute("DELETE from matches")
    DB.commit()
    DB.close()



def deletePlayers():
    """Remove all the player records from the database."""
    DB= connect()
    c = DB.cursor()
    c.execute("DELETE from matches")
    c.execute("DELETE from players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    total = 0
    DB= connect()
    c = DB.cursor()
    c.execute("SELECT count(*) as total from players")
    total = c.fetchone()[0]
    DB.close()
    return total


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB= connect()
    c = DB.cursor()
    SQL = "INSERT into players(name) values (%s);"
    # Inserts players name and checks against SQL attacks
    c.execute(SQL,(name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT id, name, wins, matches from standings")
    rows = c.fetchall()
    return rows
    DB.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    # Adds data to matches and then updates the standings table with that data
    c.execute("INSERT into matches(winner,loser) values (%s,%s)", (winner, loser))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT id, name from standings")
    pairings = []
    i = 0
    rows = c.fetchall()
    # loop builds the list of tuples that are then returned
    while i<=(len(rows)-1):
        pairings.append((rows[i][0],rows[i][1],rows[i+1][0],rows[i+1][1]))
        i = i+2 
    DB.close()
    return pairings
    