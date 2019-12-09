from flask import Blueprint, render_template, request, redirect, url_for

from flask_qa.extensions import db
from flask_qa.models import Player, Team

main = Blueprint('main', __name__)

def create_json():
    return "asdf"

@main.route('/')
def index():
    asdf=Team.query.all()
    return render_template('result.html', teams=asdf)




# user = User.query.filter_by(name=name).first()
