from flask import Flask, request, render_template, make_response,redirect, url_for, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    #link to buildMyTeam
    #Top players of the ~week
    return render_template("index.html")
@app.route('/myTeam')
def team():
    #add up to 12 players
    return render_template("myTeam.html")