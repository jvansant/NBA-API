# README

# Welcome to Josh and David's Final Project for CS 330, taught by Roman Yasinovskyy
* In this project, we scrape player and team data from espn.com and compile them into a database
* We then create an API that returns information from that database in JSON format
* Our Flask application then opens a web app that we will continue to develop, which in turn uses the API

# General Info
* Stats for players are as follows:
  * GP: Games Played
  * GS: Games Started
  * MIN: Minutes/Game
  * PTS: Points/Game
  * OR: Offensive Rebounds/Game
  * DR: Defensive Rebounds/Game
  * REB: Total Rebounds/Game
  * AST: Assists/Game
  * STL: Steals/Game
  * BLK: Blocks/Game
  * TO: Turnovers/Game
  * PF: Fouls/Game
  * AST/TO: Assist-to-Turnover Ratio
  * PER: Player Efficiency Rating
* Team stats are compiled from all players on roster, but exclude GS, MIN, and PER
