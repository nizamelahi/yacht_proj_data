import requests
from bs4 import BeautifulSoup
import json
from selenium.webdriver.common.by import By


nxt="https://www.yachtworld.com/research/"
links=[]
page=requests.get(nxt,timeout=(10,10))
soup = BeautifulSoup(page.content,"html.parser")

while True:
    print(f"extracting articles from: {nxt}")
    articles=soup.find_all("article")
    for a in articles:
        links.append(a.find('a')['href'])
    if not soup.find(class_="next"):
        break
    else:
        nxt=soup.find(class_="next").find('a')['href']
        page=requests.get(nxt,timeout=(10,10))
        soup = BeautifulSoup(page.content,"html.parser")
    # break                                                   #remove later
    
print(len(links))  

data={}
for idx,link in enumerate(links):
    try:
        print(f"scraping {idx+1}/{len(links)}")
        page=requests.get(link,timeout=(10,10))
        soup = BeautifulSoup(page.content,"html.parser")

        heading=soup.find('h1').text.strip()
        article=soup.find("div", {"id": "article-container"})
        paragraphs=article.find_all('p')
        snippets=[]
        for para in paragraphs:
            snippets.append(para.text.strip())
        
        data[heading]=snippets
    except Exception as e:
        print("_______________________________________________")
        print(e)
        print("_______________________________________________")
        continue

with open(f'data/yacht_training_data.json', 'w') as f:
    json.dump(data, f)


        
