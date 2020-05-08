import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import random
import time
from tqdm import tqdm,trange
import re

links=[]
def get_suggetion_url(num):
    base_url=f'https://www.innogov.go.kr/ucms/ogp/sug/list.do?pnum={num}&menuNo=300011&cateCd=&status1Cd=&Status2Cd=&searchText=&sugMonthTp=&orderKey=registDtDesc'
    res=requests.get(base_url)
    time.sleep(1)
    if res.status_code==200:
        html=bs(res.text,'html.parser')
        tags=html.select('#content > div.suggestion_list > ul > li>dl > dt > p > a')
        for tag in tags:
            links.append(tag.get('href'))
        num+=1
    if num==5:
        return links
    get_suggetion_url(num)
    return links
articals=[]
def get_contents(target_url):

    url=f'https://www.innogov.go.kr'+target_url
    sgid=url.split('=')[2].split('&')[0].get_text(strip=True)
    res=requests.get(url)
    if res.status_code==200:
        soup=bs(res.text,'html.parser')
        target=soup.select('#content > div.vveiw_box1 > div.vveiw_name > ul > li > dl > dd')
        area=target[0].get_text(strip=True)
        start=target[1].get_text(strip=True)
        end=target[2].get_text(strip=True)
        proposer=target[3].get_text(strip=True)
        contents=soup.select('#content > div.vveiw_box1 > div.vveiw_cont > div > pre ')[0].get_text(strip=True)

        title=soup.select(#content > div.vveiw_box1 > dl > dt')
        tilte=title[0].get_text(strip=True)
        art=[]
        art.append(sgid)
        artical.append(area)
        artical.append(title)
        artical.append(text)
        artical.append(start)
        artical.append(end)
        artical.append(proposer)
        artical.append(contents)
        time.sleep(random.randint(1,2))   
    return artical