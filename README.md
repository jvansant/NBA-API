# https://dream-team-nba.herokuapp.com/
# Welcome to our NBA Statistics API
* In this project, we scrape player and team data from espn.com and compile them into a database
* We then create an API that returns information from that database in JSON format
* Last we made an NBA DreamTeam web app that uses our API: https://dream-team-nba.herokuapp.com/

# API INFO
* [Player By ID](https://dreamteam330.herokuapp.com/api/v1.0/player/250) - JSON of player data based on id given in url
* [Team Roster](https://dreamteam330.herokuapp.com/api/v1.0/teamRoster/Lac) - JSON of all players on a team. Team based on first three letters of team's name given in url
* [General API link](https://dreamteam330.herokuapp.com/) - HTML displaying all teams and player names that have been scraped. 

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


# Created by Josh Van Sant and David Will 
