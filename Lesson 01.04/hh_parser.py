import requests as r    
from bs4 import BeautifulSoup as bs
import time
from tqdm import tqdm
import sqlite3

#pip install requests --user
#pip install beautifulsoup4 --user

class Vacancy:
    def __init__(self):
        pass
    
    def get_title(self):
        return self.__title

    def set_title(self, kek):
        self.__title = kek


headers = {"accept": "*/*", "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36"}
base_url = "https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&search_period=30&text=Python&page=0"

session = r.Session()
request = session.get(base_url, headers = headers)
if request.status_code == 200: 
    soup = bs(request.content, "html.parser")
    divs = soup.find_all("div", attrs= {"data-qa":"vacancy-serp__vacancy"})
    for div in tqdm(divs):
        try:
            title = div.find("a", attrs ={"data-qa":"vacancy-serp__vacancy-title"}).text
            href = div.find("a", attrs = {"data-qa":"vacancy-serp__vacancy-title"})['href']
            company = div.find("a", attrs = {"data-qa":"vacancy-serp__vacancy-employer"}).text
            salary = div.find("div", attrs = {"data-qa":"vacancy-serp__vacancy-compensation"}).text
            vacancy.append((title, href, company, salary))

            
        except :
            pass
        
else:
    print("Error!")



for i in vacancy:
    print(i)
