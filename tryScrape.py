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


url = "https://www.espn.com/nba/team/roster/_/name/bos/boston-celtics"

response = requests.get(url)

if response.status_code == 200 and response.headers["Content-Type"].find("html") > -1:
    raw_html = response.text
else:
    print("Bad stuff")

html = BeautifulSoup(raw_html, "html.parser")


td = html.select("td.Table__TD")


textLst = []
for x in td:
    textLst.append(x.text)
    # print(f"BREAK:{x}, TYPE: {type(x)}")

print(textLst)
