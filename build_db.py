#!/usr/bin/env python

"""Using SQLAlchemy to access a database"""

import csv
import os
from config import db
from models import Animal
from scrape import scrape


# def read_csv(filename):
#     """File format: ID Name Age Species Location"""
#     with open(f"{filename}.csv", "r") as f:
#         content = csv.reader(f)
#         next(content)
#         zoo = list(content)
#     return zoo

def timed_scrape():
    print(time.ctime())
    global players, global teams=scrape()
    updateDB(players, teams)

while True:
    timed_scrape()
    time.sleep(1200)


def build_db(filename):
    """
    Create a new database from CSV
    1. Delete the database file
    2. Create the database structure
    3. Populate the database
    """
    if os.path.exists(f"{filename}.db"):
        os.remove(f"{filename}.db")

    db.create_all()
    
    for player in global players:
        newPlayer = Player(
            

        )

    for animal in zoo:
        the_animal = Animal(
            aid=animal[0],
            name=animal[1],
            age=animal[2],
            species=animal[3],
            location=animal[4]
        )
        db.session.add(the_animal)
    db.session.commit()


def main():
    """Main function"""
    build_db("zoo")


if __name__ == "__main__":
    main()
