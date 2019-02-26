
###Anzahl und Liste der gespielten Liste
from boardgamegeek import BGGClient
bgg = BGGClient()

plays = bgg.plays(name="schrobe")
print("Anzahl gespielter Spiele: %d" % (len(plays)))

l_games_played = []

for session in plays._plays:
    l_games_played.append(session.game_name)
	
	
###Top 100 Liste, webscraped
from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page = 'https://www.boardgamegeek.com/browse/boardgame'

page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

games_top_100 =  []
for i in range(1,100):
    games_top_100.append(soup.find('div', attrs={'id': 'results_objectname'+str(i)}).get_text())
print(games_top_100)

