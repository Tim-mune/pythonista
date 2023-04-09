import requests
from bs4 import BeautifulSoup
import csv
res=requests.get('https://www.rithmschool.com/blog')
soup=BeautifulSoup(res.text,'html.parser')
articles=soup.find_all('article')

with open('blog_data.csv','w') as csv_file:
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(["title","link","date"])
    for article in articles:
        title=article.find('a').get_text()
    url=article.find('a')['href']
    time=article.find('time')['datetime']
    csv_writer.writerow([title,url,time])
    

