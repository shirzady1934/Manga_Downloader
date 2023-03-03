import sys
import requests
import cloudscraper
from bs4 import BeautifulSoup

requests.urllib3.disable_warnings()
#proxy = 'http://181.119.69.153:3128'
proxy = 'http://127.0.0.1:8118'

proxies = {
        'http': proxy, 
        'https': proxy,
}

url = sys.argv[1]
#res = requests.get(url)
sc = cloudscraper.create_scraper()
res = sc.get(url) 
soup = BeautifulSoup(res.text, features='lxml')

links = []
#for image in soup.findAll('img'):
for image in soup.find_all('img', attrs={'class': 'fixed-ratio-content'}):
    try:
        links.append(image['src']).replace('\r', '')
    except:
        pass
print('\n'.join(links))

for counter in range(len(links)):
    with open('%d.jpg' % counter, 'wb') as f:
        im = requests.get(links[counter], stream=True, timeout=10)#, verify=False)#, proxies=proxies)
        f.write(im.content)

