from flask import Flask, request, render_template, make_response,redirect, url_for, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    #link to buildMyTeam
    #Top players of the ~week
@app.route('/myTeam')
def team():
    #add up to 12 players