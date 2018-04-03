import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.sina.com.cn/')
res.encoding='utf-8'
soup = BeautifulSoup(res.text,'html.parser')
for news in soup.select('.newslist'):
    href=news.select('a')[0]['href']
    text=news.select('a')[0].text
    print(text+','+href)