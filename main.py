import subprocess
import requests
from bs4 import BeautifulSoup

base = 'https://onepiecechapters.com'
url = 'https://onepiecechapters.com/mangas/2/bleach?&date=8-2-2023-14'
res = requests.get(url)
soup = BeautifulSoup(res.text, features='lxml')
fnd = soup.find_all('a', attrs={'class':"block border border-border bg-card mb-3 p-3 rounded"})
fnd = fnd[::-1]
cnt = 401
end = 500
ftrue = False
for i in range(len(fnd)):
    link = fnd[i]['href']
    epid = link.split('-')[-1]
    try:
        if int(epid) != cnt and not ftrue:
            continue
    except:
        if int(epid.split('.')[0]) != cnt and not ftrue:
            continue
    ftrue = True
    cmd = "./chapters.sh %s %s" % (base+link, epid)
    rt = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rt.wait()
    print("Cahpter %s done!" % epid)
    try:
        if int(epid) == end:
            break
    except:
        if int(epid.split('.')[0]) == end:
            break



