from flask import Blueprint, render_template, request, redirect, url_for

from flask_qa.extensions import db
from flask_qa.models import Player, Team

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user = Player(
        id =0,
        name = "bob",
        team = "lakers",
        gp = 1,
        gs = 2,
        min =3,
        pts = 4,
        ro = 5,
        dr = 6,
        reb = 7,
        ast = 8,
        stl = 9,
        blk = 10,
        to = 11,
        pf = 12,
        astTo = 13,
        per = 14
        )
    db.session.add(user)
    db.session.commit()
    asdf=Player.query.all()
    return render_template('result.html', result=asdf)




# user = User.query.filter_by(name=name).first()
