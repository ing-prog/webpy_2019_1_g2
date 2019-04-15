import requests as r    
from bs4 import BeautifulSoup as bs
import time
from tqdm import tqdm
import sqlite3
from vacancy import Vacancy
import pandas as pd
#pip install pandas --user



headers = {"accept":"*/*" ,
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}


base_url = "https://hh.ru/search/vacancy?search_period=30&clusters=true&area=1&text=Python&enable_snippets=true"

session = r.Session()
request = session.get(base_url, headers=headers)
vacancy_list = []

if request.status_code == 200: 
    print("It's ok!")
    soup = bs(request.content, "html.parser")
    divs = soup.find_all("div", attrs= {"data-qa":"vacancy-serp__vacancy"})
    
    for div in divs:
        try:
            title = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'}).text
            href = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'})['href']
            company = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
            requirement = div.find("div", attrs ={'data-qa':'vacancy-serp__vacancy_snippet_requirement'}).text
            salary = div.find('div',attrs = {'data-qa':'vacancy-serp__vacancy-compensation'}).text
            vac = Vacancy(title = title, href = href, company = company,  requirement = requirement,salary = salary)
            vacancy_list.append(vac)

            
        
        except :
            pass
        

    for i in vacancy_list:
        print(i.get_title(), i.get_salary(), i.get_requirement())


        








    data2 = {"title":[x.get_title() for x in vacancy_list],
            "href" :[x.get_href() for x in vacancy_list],
            "company" : [x.get_company() for x in vacancy_list],
            "requirement" : [x.get_requirement() for x in vacancy_list],
            "salary": [x.get_salary() for x in vacancy_list] }

    df = pd.DataFrame(data = data2)
    print(df)
    df.to_csv("kek.csv")
    
        
       
        

else:
    print("Error!")