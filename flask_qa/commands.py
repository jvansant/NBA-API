import click
import os
import time
from flask.cli import with_appcontext
from .extensions import db
from .models import Player, Team
from .scrape import scrape
from.build_db import build_db


def timed_scrape():
    print(time.ctime(), " SCRAPING")
    players, teams = scrape()
    build_db(players, teams)

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    while True:
        timed_scrape()
        time.sleep(1200)
   
