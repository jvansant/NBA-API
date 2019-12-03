from flask import Flask, request, render_template, make_response,redirect, url_for, send_from_directory, jsonify

app = Flask(__name__)

def initDataBase():
    

@app.route('/api/v1/<int:id>')
def player():
    #scrape data