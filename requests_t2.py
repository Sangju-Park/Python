
import requests
from bs4 import BeautifulSoup

url="https://nid.naver.com/nidlogin.login"

lines='''\
enctp: 1
encpw: 

encnm: 100013589
svctype: 0
svc: 
viewtype: 0
locale: ko_KR
postDataKey: 
smart_LEVEL: -1
logintp: 
url: https://www.naver.com
localechange: 
ls: 
xid: 
pre_id: 
resp:
ru: 
id:matrixsj
pw:nagarjuna6\
'''.splitlines()

lines_change=[]

for line in lines:
    line=line.replace(" ","")
    lines_change.append(line)

data={}
for line in lines_change:
    key,value=line.split(':',1)
    data[key]=value

sess=requests.Session()
response= requests.post(url,data=data)
html=response.text
# print(response)
# soup=BeautifulSoup(html,'html.parser')
print(html)
# for tag in soup.select('.private.user_name'):
#     print(tag.text.strip())





# results=soup.select_one("span.blind")
# print(results.text)

# results=soup.select_one("div.private > span.user strong")
# #print(results.text)