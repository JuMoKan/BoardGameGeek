
###Anzahl und Liste der gespielten Liste
from boardgamegeek import BGGClient
bgg = BGGClient()

playerName = "schrobe"

plays = bgg.plays(name=playerName)
print("Anzahl gespielter Spiele: %d" % (len(plays)))


# maps game IDs to the dictionary: {name, rating, rank}
gameDict = {}
for play in plays._plays:
    gameId = play.game_id
    if(gameId == 1219 or gameId == 432): # these games have invalid data
        continue
    game = bgg.game(game_id=gameId)
    name = game._name
    rating = game._data['stats']['bayesaverage']
    ranks = game._data['stats']['ranks']
    # For each game, different ranks are stored depending on a category. We want the rank in the category 'boardgame'
    boardgameRank = next(x for x in ranks if x['name']=='boardgame')['value']
    # For each entry in our dictionary, the value is another dictionary that has entries for name, rating and rank
    gameDict[gameId] = {}
    valuesDict = gameDict[gameId]
    valuesDict['name'] = name
    valuesDict['rating'] = rating
    valuesDict['rank'] = boardgameRank
    print(str(boardgameRank)+" : "+ str(rating)+ " : "+name) 
	
# "Copy" the games dictionary into a list that is sorted by the 'rank'
# x[1] means: get the value of the dictionary
sortedGames = sorted(gameDict.items(), key=lambda x: x[1]['rank'])

for gameTuple in sortedGames:
    game = gameTuple[1]
    print(str(game['rank'])+":\t"+ str(game['rating'])+ ":\t"+game['name']) 


'''	
###Top 100 Liste, webscraped
from urllib2 import urlopen
from bs4 import BeautifulSoup
quote_page = 'https://www.boardgamegeek.com/browse/boardgame'

page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
#print(soup)

games_top_100 =  []
for i in range(1,100):
    games_top_100.append(soup.find('div', attrs={'id': 'results_objectname'+str(i)}).get_text())
print(games_top_100)
'''
