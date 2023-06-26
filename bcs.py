import requests
import pandas as pd


def randomEpisode(baseurl, resourceEpisodes):
    r = requests.get(baseurl + resourceEpisodes)
    return r.json()



def getCharacter(response):
    characterlist = []
    for char in response['characters']:
        characterlist.append(char)
    return characterlist


def getSatus(charlist):
    deadCharacters = []
    for char in charlist:
        checkStatus = requests.get(baseurl + resourceCharacters + f'?name={char}' + f'&status=Alive')
        data = checkStatus.json()
        for item in data:
            if isinstance(item, dict) and 'name' in item and 'status' in item:
                dic = {
                    'name': item['name'],
                    'status': item['status']
                }
                deadCharacters.append(dic)
    return deadCharacters



def getQuote (statusData):
    deadCharactersQ= []
    for data in statusData:
        char = list(data.values())[0]
        quote = requests.get(baseurl + resourceQuote + f'?author={char}')
        quoteDataCharacter = quote.json()
        for item in quoteDataCharacter:
            dic = {
                'author': item['author'],
                'quote': item['quote']
            }
        deadCharactersQ.append(dic)
    return print(deadCharactersQ)





baseurl = "https://bettercallsaul-api.onrender.com"
resourceEpisodes = "/episodes/random"
resourceCharacters = "/characters"
resourceQuote = "/quotes"


rEp = randomEpisode(baseurl,resourceEpisodes)
charlist = getCharacter(rEp)
statusData = getSatus(charlist)
quoteData = getQuote(statusData)
