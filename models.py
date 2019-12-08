#!/usr/bin/env python
"""Data models"""

from config import db, ma

class Player(db.Model):
    __tablename__ = "PLAYER"
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    team = db.Column(db.String)
    gp = db.Column(db.Integer)
    gs = db.Column(db.Integer)
    min = db.Column(db.Float)
    pts = db.Column(db.Float)
    ro = db.Column(db.Float)
    dr = db.Column(db.Float)
    reb = db.Column(db.Float)
    ast = db.Column(db.Float)
    stl = db.Column(db.Float)
    blk = db.Column(db.Float)
    to = db.Column(db.Float)
    pf = db.Column(db.Float)
    astTo = db.Column(db.Float)
    per = db.Column(db.Float)


class PlayerSchema(ma.ModelSchema):
    class Meta:
        model = Player
        sqla_session = db.session


# class Team(db.Model):
#     __tablename__ = "PLAYER"
#     tid = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     gp = db.Column(db.Integer)
#     pts = db.Column(db.Float)
#     ro = db.Column(db.Float)
#     dr = db.Column(db.Float)
#     reb = db.Column(db.Float)
#     ast = db.Column(db.Float)
#     stl = db.Column(db.Float)
#     blk = db.Column(db.Float)
#     to = db.Column(db.Float)
#     pf = db.Column(db.Float)
#     astTo = db.Column(db.Float)


# class TeamSchema(ma.ModelSchema):
#     class Meta:
#         model = Team
#         sqla_session = db.session