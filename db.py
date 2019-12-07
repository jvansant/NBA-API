from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

app=Flask(__name__)
#yeah idk
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://vansjo01:knuth.luther.edu/home/LC/vansjo01'
db =SQLAlchemy(app)

@app.route('/')

def initDB():
    return "asdf"

def updateDB():
    return"qwer"

def timed_scrape():
    print(time.ctime())
    players, teams=scrape()
    updateDB(players, teams)

while True:
    timed_scrape()
    time.sleep(1200)

    