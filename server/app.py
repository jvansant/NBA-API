from flask import Flask, request, render_template, make_response,redirect, url_for, send_from_directory, jsonify, request
from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup

app = Flask(__name__)

BASE_PLAYERS = "https://www.nba.com/players"
BASE_TEAMS = "https://www.nba.com/teams"

def get_players():
    """Get all player links in NBA"""
    player_links={}
    response = requests.get(BASE_PLAYERS)

    if (
        response.status_code == 200
        and response.headers["Content-Type"].find("html") > -1
    ):
        raw_html = response.text
    else:
        print("Bad stuff")

    html = BeautifulSoup(raw_html, "html.parser")
    
    for player in html.select("section#block-league-content > section.nba-player-index__row > section.nba-player-index__trending-item"):
        badtags=player.select("a.nba-player-index__team-image")
        alltags=player.select("a")
        tags=Diff(alltags, badtags)
        for tag in tags:
            p_url=tag["href"]
            p_name=tag["title"]
            player_links[p_name]=p_url
            
    return player_links

def get_teams():
    """Get all teams in NBA"""
    team_links={}
    response = requests.get(BASE_TEAMS)

    if (
        response.status_code == 200
        and response.headers["Content-Type"].find("html") > -1
    ):
        raw_html = response.text
    else:
        print("Bad stuff")

    html = BeautifulSoup(raw_html, "html.parser")
    
    for team_div in html.find_all("div", class_="team__list"):
        a=team_div.select("a")
        link=a[0]["href"]
        name=a[0].contents[0]
        team_links[name]=link

    return team_links

def scrape_team_data(url):
    print("asdf")
    driver = webdriver.Chrome('/home/administrator/Desktop/330FinalProject/server/chromedriver') 
    driver.get(url) 
    html = driver.page_source
    html = BeautifulSoup(html, "html.parser")
    
    for stat in html.find_all("team-info-stats"):
        print(stat,"\n")

def timed_scrape():
    print(time.ctime())
    scrape_team_data("https://www.nba.com/teams/hawks")

while True:
    timed_scrape()
    time.sleep(1200)

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 



# scrape_team_data("https://www.nba.com/teams/hawks")


# def init_db():
#     return "ASDF"

# @app.route('/')
# def base():
#     return render_template("index.html")

# @app.route('/api/v1/<int:id>')
# def player():
#     #scrape data

players=get_players()
teams=get_teams()