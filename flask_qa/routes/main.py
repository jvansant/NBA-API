from flask import Flask, Blueprint, request, render_template, make_response,redirect, url_for, send_from_directory, jsonify
from flask_qa.extensions import db
from flask_qa.models import Player, Team
import psycopg2
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    asdf=Team.query.all()
    qwer=Player.query.all()
    return render_template('result.html', teams=asdf, players=qwer)

@main.route('/api/v1.0/team/<int:id>')
def team(id):
    result = Team.query.filter(Team.id==id).all()
    teamData=jsonify(id=result.id, name=result.name,  gp=result.id, pts=result.pts, ro=result.ro, dr=result.dr, reb=result.reb, ast=result.ast, stl=result.stl, blk=result.blk)
    return render_template('json.html', jteamData=teamData)

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
