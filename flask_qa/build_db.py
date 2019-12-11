#!/usr/bin/env python

"""Using SQLAlchemy to access a database"""

import os
from .extensions import db
from .models import Player, Team

def build_db(players, teams):
    """
    Create a new database from scraped dictionaries
    1. Delete the database file
    2. Create the database structure
    3. Populate the database
    """
    db.session.remove()
    db.drop_all()
    db.create_all()
    for player in players:
        if players[player]["TEAM"]=="Los Angeles Clippers":
            teab='Lac'
        elif players[player]["TEAM"]=="Los Angeles Lakers":
            teab='Lal'
        else:
            teab=players[player]["TEAM"][0:3]

        if players[player]["AST/TO"]>10000:
            ast_to=players[player]["AST"]
        else:
            ast_to=players[player]["AST/TO"]
        newPlayer = Player(
            id = players[player]["ID"],
            name = player,
            team = players[player]["TEAM"],
            teamabr = teab,
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
            astTo = ast_to,
            per = players[player]["PER"]
        )
        db.session.add(newPlayer)
    for team in teams:
        newTeam = Team(
            id = teams[team]["ID"],
            name = team,
            gp = teams[team]["GP"],
            pts = teams[team]["PTS"],
            ro = teams[team]["OR"],
            dr = teams[team]["DR"],
            reb = teams[team]["REB"],
            ast = teams[team]["AST"],
            stl = teams[team]["STL"],
            blk = teams[team]["BLK"],
            to = teams[team]["TO"],
            pf = teams[team]["PF"],
            astTo = teams[team]["AST/TO"]
        )
        db.session.add(newTeam)
    db.session.commit()