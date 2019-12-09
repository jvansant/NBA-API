from flask import Flask, Blueprint, request, render_template, make_response,redirect, url_for, send_from_directory, jsonify
from flask_qa.extensions import db
from flask_qa.models import Player, Team
import psycopg2
import os

main = Blueprint('main', __name__)

def get_data_from_db(query: str):
    DATABASE_URL = os.environ['DATABASE_URL']
    try:
       conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    except:
        raise ConnectionError("Bad stuff")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

@main.route('/')
def index():
    asdf=Team.query.all()
    qwer=Player.query.all()
    return render_template('result.html', teams=asdf, players=qwer)

@main.route('/api/v1.0/team/')
def team():
    query = "select * from Player"
    query2 = "select * from Team"
    result = get_data_from_db(query2)
    result2 = get_data_from_db(query)
    print("AESGAWEGAEGAW")
    print(rows)
    return render_template('result.html', teams=result, players=result2)

# Team.query.filter_by(name=name).first()


# @app.route("/", methods=["GET", "POST"])
# def index():
#         query = "select * from player"
#         result = get_data_from_db(query, "Player")
#         print(result)
#         return render_template("result.html", rows=result)


# @app.route('/api/v1/players/<int:id>')
# def player():
#     jokes=pyjokes.get_jokes("en", "all")
#     rand=random.randrange(0,201)
#     joke=jokes[rand]
#     joke_in_dict ={"joke": joke}
#     asdf =jsonify(joke_in_dict)
#     return "<html><body>"+asdf+"</body></html>"

# @app.route('/api/v1/teams/<int:id>')
# def specific_joke(id):
#     jokes=pyjokes.get_jokes("en", "all")
#     joke=jokes[id]
#     joke_in_dict ={"joke": joke}
#     return jsonify(joke_in_dict)
