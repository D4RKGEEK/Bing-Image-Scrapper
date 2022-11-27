import requests
from bs4 import BeautifulSoup
seartext = input("enter the search term: ")
count = input("Enter the number of images you need:")
adlt = 'on' # can be set to 'moderate'
sear=seartext.strip()
sear=sear.replace(' ','+')
URL='https://bing.com/images/search?q=' + sear + '&safeSearch=' + adlt + '&count=' + count
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)
results=[]
soup = BeautifulSoup(resp.content, "html.parser")
wow = soup.find_all('a',class_='iusc')
c = 0
for i in wow:
        try:
            ok = eval(i['m'])['murl']
            results.append(ok)
        except:
            pass

for i in range(int(count)):
    print(results[i])
