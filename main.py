import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news?p=1')
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.select('.titleline>a') #to get the tags associated with the news title and links
subtexts = soup.select('.subtext') #to get the whole subtext tags, so we can filter out later ones that have score
votes = []


#to fill the votes array
#to filter out subtexts without and with score
for subtext in subtexts:
    if subtext.find('span', class_ = 'score'):
        votes.append(subtext.find('span', class_ = 'score'))
    else:
        votes.append(0)


#fetches news's with >= 100 votes
def get_news(links, votes):
    news = []
    for index, vote in enumerate(votes):
        vote = int(vote.text.split(' ')[0]) #cleaning
        if vote >= 100:
            dict = {
                'title': links[index].text, #to grab the title
                'link': links[index].get('href'), #to get the link associated with the title
                'votes': vote
            }
            news.append(dict)
    news.sort(key = lambda x:x['votes'], reverse=True) #sorting based on the no.of votes in desc order
    return news



print(get_news(links, votes))








