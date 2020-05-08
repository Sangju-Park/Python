from bs4 import BeautifulSoup
import urllib.request
  
user_agent = 'Mozilla/5.0 (Windows NT 7.0; WOW64; rv:12.0) Gecko/20100101 Firefox/15.0'
data = {"Source_Saup_No_11_11_7":"1010421058", "Target_Saup_No_11_11_7":"2260848825"} #data는 POST 형태로 넘겨질 데이터. Source_Saup_No_11_11_7, Target_Saup_No_11_11_7 은 매일 값이 바뀌므로 국세청에서 확인 필요

p_data = urllib.parse.urlencode(data).encode('cp949')

url = 'https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId='
 
req = urllib.request.Request(url, p_data)
req.add_header('user-agent', user_agent)

res = urllib.request.urlopen(req)
print(res.info())

s = res.read().decode('utf-8')
soup = BeautifulSoup(s)
print(soup)
 
a = soup.find(None, {'id':'cont_table_01'})
b = a.findAll('id', None)

for i in b:
 print(i.text.strip())