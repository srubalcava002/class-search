from bs4 import BeautifulSoup as bs
import requests


# VALUES FOR TESTING
term = '2207'
prefix = 'BIO'
number = '100'
location = 'TEMPE'
avail = 'all'

# term number seems to be unique to each term
search_url = f'https://webapp4.asu.edu/catalog/myclasslistresults?t={term}&s={prefix}&n={number}&hon=F&promod=F&c={location}&e={avail}&page=1'

query = bs(requests.get(search_url).content, 'html.parser')
classname = query.find('td', class_='subjectNumberColumnValue nowrap')
print(classname.find('span').text)

seats_open = query.find_all('td', class_='availableSeatsColumnValue')
# print(query.find('div', class_='col-xs-3'))

for string in query.find('div', class_='col-xs-3'):
    print(int(string))
