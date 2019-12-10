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

@main.route('/api/v1.0/team/<int:teamId>')
def team(teamId):
    result = Team.query.filter_by(id=teamId).first()
    teamData=jsonify(id=result.id, name=result.name,  gp=result.gp, pts=result.pts, ro=result.ro, dr=result.dr, reb=result.reb, ast=result.ast, stl=result.stl, blk=result.blk)
    return make_response(teamData, 201)

@main.route('/api/v1.0/player/<int:playerId>')
def player(playerId):
    result = Player.query.filter_by(id=playerId).first()
    playerData=jsonify(id=result.id, name=result.name, team=result.team, gp=result.gp, gs=result.gs, min=result.min, pts=result.pts, ro=result.ro, dr=result.dr, reb=result.reb, ast=result.ast, stl=result.stl, blk=result.blk, to=result.to, pf=result.pf, ast_to=result.astTo, per=result.per)
    return make_response(playerData, 201)
