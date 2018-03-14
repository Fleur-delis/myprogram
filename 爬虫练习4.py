#爬取时间，正文以及简略写法
import requests
from bs4 import BeautifulSoup
from datetime import datetime
res = requests.get('http://news.sina.com.cn/china/xlxw/2018-03-14/doc-ifyscsmv6573968.shtml')
res.encoding='utf-8'
soup = BeautifulSoup(res.text,'html.parser')
date = soup.select('.date-source')[0].contents[1].text
source = soup.select('.date-source')[0].contents[3].text
dt = datetime.strptime(date,'%Y年%m月%d日 %H:%M')
print(dt,source)
'''article=[]
for p in soup.select('.article p')[:-1]:
    article.append(p.text.strip())
'----'.join(article)
'''
'----'.join([p.text.strip() for p in soup.select('.article p')[:-1]])