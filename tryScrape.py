import requests
from bs4 import BeautifulSoup

# url = "https://www.luther.edu/catalog/curriculum/"

# response = requests.get(url)

# # print(response.text)
# print(response.status_code)
# print(response.headers)
# print(response.headers["Content-Type"].split("; ")[0])

# if response.status_code == 200 and response.headers["Content-Type"].find("html") > -1:
#     raw_html = response.text
# else:
#     print("Bad stuff")

# html = BeautifulSoup(raw_html, "html.parser")
# print(html)

# for program in html.select("div#contentSections ul > li > h4 > a"):
#     p_name = program.text
#     p_url = program["href"]
#     print(f"{p_name}: {p_url}")

url = "https://www.espn.com/nba/team/stats/_/name/"
teams = ["bos","bkn","ny","phi","tor","chi","cle","det","ind","mil","den","min","okc","por","utah","gs","lac","lal","phx","sac","atl","cha","mia","orl","wsh","dal","hou","mem","no","sa"]

allPlayerLinks = []
url = "https://www.espn.com/nba/team/stats/_/name/mil"
response = requests.get(url)

if response.status_code == 200 and response.headers["Content-Type"].find("html") > -1:
    raw_html = response.text
else:
    print("Bad stuff")

html = BeautifulSoup(raw_html, "html.parser")
players = html.select("tbody.Table__TBODY > tr.Table__TR > td.Table__TD > span > a.AnchorLink")

# playerList = []
# for item in players:
#     playerList.append(item.text)
# playerList = list(set(playerList))

# positions = html.select("tbody.Table__TBODY > tr.Table__TR > td.Table__TD > span > span.font10")
# positionList = []
# for position in positions:
#     positionList.append(position.text)

# positionList = positionList[:len(playerList)]

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

playerToStats = {}

statHeaders = ["GP","GS","MIN","PTS","OR","DR","REB","AST","STL","BLK","TO","PF","AST/TO","PER"]

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
    for j in range(len(statHeaders)):
        statDict[statHeaders[j]] = stats[j]
    statDict["POSITION"] = positions[i]

    playerToStats[player] = statDict

print(playerToStats)