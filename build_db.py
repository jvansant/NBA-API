#!/usr/bin/env python

"""Using SQLAlchemy to access a database"""

import csv
import os
from config import db
from models import Player
from scrape import scrape
import time

global players
global teams
players, teams = scrape()
build_db("player")
# def timed_scrape():
#     print(time.ctime())
#     global players
#     global teams
#     players, teams = scrape()
#     build_db("player")
    

# while True:
#     timed_scrape()
#     time.sleep(1200)


def build_db(filename):
    """
    Create a new database from CSV
    1. Delete the database file
    2. Create the database structure
    3. Populate the database
    """
    
    if os.path.exists("players.db"):
        print("do we get here?")
        os.remove("players.db")
    db.create_all()
    global players
    for player in players:
        newPlayer = Player(
            pid = players[player]["ID"],
            name = player,
            team = players[player]["TEAM"],
            gp = players[player]["GP"],
            gs = players[player]["GS"],
            min = players[player]["MIN"],
            pts = players[player]["PTS"],
            ro = players[player]["OR"],
            dr = players[player]["DR"],
            reb = players[player]["REB"],
            ast = players[player]["AST"],
            stl = players[player]["STL"],
            blk = players[player]["BLK"],
            to = players[player]["TO"],
            pf = players[player]["PF"],
            astTo = players[player]["AST/TO"],
            per = players[player]["PER"]
        )
        db.session.add(newPlayer)
    db.session.commit()

    # for animal in zoo:
    #     the_animal = Animal(
    #         aid=animal[0],
    #         name=animal[1],
    #         age=animal[2],
    #         species=animal[3],
    #         location=animal[4]
    #     )
    #     db.session.add(the_animal)
    # db.session.commit()


def main():
    """Main function"""


if __name__ == "__main__":
    main()
