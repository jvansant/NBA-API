import requests
from bs4 import BeautifulSoup

teams = ["bos","bkn","ny","phi","tor","chi","cle","det","ind","mil","den","min","okc","por","utah","gs","lac","lal","phx","sac","atl","cha","mia","orl","wsh","dal","hou","mem","no","sa"]
# For now I'm using this dict to put more meaningful info in the player team attribute. Might try to scrape it instead, we'll see.
fullTeamDict = {
    "bos": "Boston Celtics",
    "bkn": "Brooklyn Nets",
    "ny": "New York Knicks",
    "phi": "Philadelphia 76ers",
    "tor": "Toronto Raptors",
    "chi": "Chicago Bulls",
    "cle": "Cleveland Cavaliers",
    "det": "Detroit Pistons",
    "ind": "Indiana Pacers",
    "mil": "Milwaukee Bucks",
    "den": "Denver Nuggets",
    "min": "Minnesota Timberwolves",
    "okc": "Oklahoma City Thunder",
    "por": "Portland Trailblazers",
    "utah": "Utah Jazz",
    "gs": "Golden State Warriors",
    "lac": "Los Angeles Clippers",
    "lal": "Los Angeles Lakers",
    "phx": "Phoenix Suns",
    "sac": "Sacramento Kings",
    "atl": "Atlanta Hawks",
    "cha": "Charlotte Hornets",
    "mia": "Miami Heat",
    "orl": "Orlando Magic",
    "wsh": "Washington Wizards",
    "dal": "Dallas Mavericks",
    "hou": "Houston Rockets",
    "mem": "Memphis Grizzlies",
    "no": "New Orleans Pelicans",
    "sa": "San Antonio Spurs"
}
# Hey Josh--shot you a text but just a reminder:
# playerToStats is a dictionary with players (strings) as keys and their stats (dicts) as values.
# teamToStats is a dictionary with teams (strings) as keys and their stats (dicts) as values.
# Stats that don't make sense for teams--games started, minutes, PER, etc--are not included
# This way we're primed to get the database created, and then we're off to the races
# I *think* this is all the scraping we'll need, at least for now.

playerToStats = {}
teamToStats = {}
for teamExtension in teams:
    url = "https://www.espn.com/nba/team/stats/_/name/"
    teamUrl = url + teamExtension
    response = requests.get(teamUrl)

    if response.status_code == 200 and response.headers["Content-Type"].find("html") > -1:
        raw_html = response.text
    else:
        print("Bad stuff")

    html = BeautifulSoup(raw_html, "html.parser")
    players = html.select("tbody.Table__TBODY > tr.Table__TR > td.Table__TD > span > a.AnchorLink")
    stats = html.select("tbody.Table__TBODY > tr.Table__TR")

    statLst = []
    for stat in stats:
        for item in (stat.select("td.Table__TD > span")):
            statLst.append(item.text)

    firstItem = statLst[0]
    stopPoint = statLst[1:].index(firstItem)
    statLst = statLst[:stopPoint]

    totalIndex = statLst.index("Total") + 1
    realPlayerList = statLst[:totalIndex]
    allStats = statLst[totalIndex:] + [""]

    statsByPlayer = []
    totalLoops = 14 * len(realPlayerList)
    
    current = 0
    for i in range(14, totalLoops+14, 14):
        statsByPlayer.append(allStats[current:i])
        current = i

    teamStats = statsByPlayer[-1]
    statHeaders = ["GP","GS","MIN","PTS","OR","DR","REB","AST","STL","BLK","TO","PF","AST/TO","PER"]
    teamDict = {}

    for i in range(len(statHeaders)):
        if teamStats[i] != "":
            teamDict[statHeaders[i]] = teamStats[i]            

    teamToStats[fullTeamDict[teamExtension]] = teamDict

    playersWithoutPos = []
    positions = []
    for player in realPlayerList:
        if player != "Total":
            if player[-1] == "C":
                position = player[-1]
                player = player[:-2]
            else:
                position = player[-2:]
                player = player[:-3]
            positions.append(position)
            playersWithoutPos.append(player)
    
    for i in range(len(playersWithoutPos)):
        player = playersWithoutPos[i]
        stats = statsByPlayer[i]
        statDict = {}
        statDict["POSITION"] = positions[i]
        statDict["TEAM"] = fullTeamDict[teamExtension]
        for j in range(len(statHeaders)):
            statDict[statHeaders[j]] = stats[j]
        playerToStats[player] = statDict