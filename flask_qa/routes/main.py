from flask import Blueprint, render_template, request, redirect, url_for

from flask_qa.extensions import db
from flask_qa.models import Player, Team

main = Blueprint('main', __name__)

@main.route('/')
def index():
    asdf=Player.query.all()
    return render_template('result.html', result=asdf)

# user = User.query.filter_by(name=name).first()
