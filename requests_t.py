
import requests
from bs4 import BeautifulSoup
import time

url="https://nid.naver.com/nidlogin.login"

lines='''\
bvsd: {"uuid":"202c7372-0da1-41cc-b59c-353fffa9c5a4","encData":"N4IgrmCWAmIFwgEwAZEGMDsBmDiC0y0AhgIx4AsJaaeARgKwCcNW9WAZp0c/UeSABoQANwCmAJwDOkAPYA7eCGQA6espKCQkSQBUZYNAAsAIqOGQ0o+OyIAbSaKEBrUQE8AygBdxMl5PgA2qAwiiFCkHIADmCeAJJynhLCdgAyMgDm/nBBIETwyEJoigC2mrBwyAC+AqB5cIgk5IUleULlJNW18CQoBSBFCMVEnmXwiJ25Y8hN/S3eo3BYE3UkAGwzAyBD3pAL5Mvd9IjNg8PikAAeC/QHcGuMJ1tnl/5t8Ku3JNiP2+cXkgArBYYSoAXWcbi8PhcaUygS6FSEtEUsEekA0bwQGAwIFuAA4+siEGBNJt0QsQNjcTVJvU1kiUaTQogKat6NSESQsKsGcSmQhICzMSA2RzaT1kITGWisBS8fxbt8QETwPytLLhfKxXUUPReSBUbMBfxNSz8Vh9SS0SaDYo8WaaSt1vrDWT2cLsNr4Iw9crFFajVp3basbLPvQSC61ZBVnK8V64ATLdHY5r459Vnio2icZqw47usgLX6+Tm5fnORhfSrXaF4x6FQW4EqVQGyfWQ5SFeCtHJIJ5IHYAGp2MBWBCkmTFSK2USJEe2MdzP6AzTjmz2UQTEIISIAd00EWicQSSVSGSyOTqfU2CyqTYaN8UCw6TZ6X0eC3GTawKE/mKWJtGFYf8Q32H8GlA8objfRgnwnTEPgfEgs0DYFbkQegNmfTE8VuShIzQzFGDBCEPG8XxRFhS8ESlBBawFZAKQTDBUNbaMmOFBMGmraVA3JLjPj/EtVTRDFOwTd8eREhitCFCTPmmZM0Xk8oQATX86NtGVmM+LllP4jUFKA7ls34m01ITRhpPY61dIgrTZMgYNLPxNj/WjFzn0+RhCJrFN7IRFsPLRVNjIRBoMDMslc3C2lcAMmLAtpTDePo6MO1coCopEts62SupyGQB4ZOjRgCsLGZbP48rBLfcgiuixQAFEADkdGagAlXSewiftB1sBclwQ/opxnOdRCG8d1KEcdvDHUiQBkc5RASYZZDkLJQHYSApE8AB5Fa1oHeR4ARBqqvgC6Tgu6oQFsIhJAOo7PHW064HOhreWuo1bru4oZBOzazpAHa9oAWUBjaQaIahRFncQ3oUD7aR+okfoGW6hFhywEaR+I0EXaAInSABxRHzE8VwYaur6Swx2n9juh6nshoGYbhvH2ZRwq6fRunMYau6cfhiR8bkQmwGJuQyYp/tqZ5xnvoFxnKjVoQAbABxAiUAAfZBdfoPFVgwXWUFWfXNBIfWbbxXWwsQG2SANnpdY7LAnetrldZ6TRyCd+hdd/M2O0Dl3GDNwPuU0C2XYtrBrcoTRTZdwPVmtvEjLtl3TYaIOOwjnOfetxBYudp3c91m0SGtuOzftq3HaL/3q49ovXeDRonbtlBDatsOfYttk3at2OfbtjALZrq2U5902fQboQUKdi3yFjq3C59/3g84pADZdu2SDDzQ87ri28HkxAm7nn3dbwcTEDb4va7vh//YNsf75Pgevhti+T7Hr/A2/8hClwDn/B+2dx6fwfpvI+EDNBYH3oPeuFBEEvzWKg+SO8b5N0QU/I+LtLZCCwO/G+tdEE/wtsfEhgC7Zt0QbPcggcU6IKgabHAxCQBYDgWnA28kirgIaI7dYfsMH0Jrj7Uhftr5d2HogG05ACE91NmFBqFdb672YZ7YBFChBr1tnfD2AjZ7e3vmbP2UDe54A9kZcgcD/Y2IsUIegyDMHmPEhGW+mFkG7yOPXZ2vjNBsCdg1Rgds8DWWtvfNgwSyGSOiaHH+UdX6h0AbPSJwTTGf1qiAI2GjgEoGCXA02gcL5GVWG4020SFExwwSwu+j8Y6yI4XfWKqxlG3xsTHMh6xkFfyEMPA2pDX5cNWGPK+ozd4mxtkbMpHswqZhtqbSJPtplwMdvfL28kMBVMaSXIyGAMHn12YbXeuBu533IPQw5T8I4X39ihZOZDWCrE2doxoycf5e2AcGSeK8zYezQUIbE4DuR3z+VA5eYDukgrgRHTCXCCShKrkijBpsVlZxaW7K5mhM4AvcUfPF8TqnRKJUIPEVDUWZIpekv+YU8Sz04WSvFULjFIpKVgzQcEAXAKMr5S5wDYqMGxYU7lT8cEDJAIweJA88DCp/pvPABdAFyoLqY6pd8C5QtXnfXJjBeFBzaVbSUGigXOxNeI+2r9d7O1kYHMpvsl5FidhHcu99bXTBRSssKztklcudYA+OjSTUatQUZZ2ULTaOM7sVAFjiI3lyLps8SNcvaAqfra12BsB5ZvZT0TNVsu4GyUV01N8CXZkNhSAGuY9WBTKLaY+UoypU1ysVW+SNdN5QNbb3VOf9O2nxvmKpekyXZepHTWx+t8uS5sbmQxAY9bWIsds7Wey662TPMb22eyLdGNysYUoxjc4Hnz0TWpBNtEARJZUvBOTsU1cK5Ni7dqasBP2vS2t9ZCwkRwRVbetLtHa5wA3Qo1ndOH9sdp2rAUDL38IA92p2VtBFFxdihl+WEbbV3INfKBvrS1AdGbkxo8T7lus7douuOaUN0ooLrMu5Am2jMo1C3pKG4ERKHv3PZ5jO5eP7RfH2/dZGlo8f3D2Gd139wXUu/ugdV2UBtkxHstAfB7gcOIAAYiTCQkRzgJAABKPUMIocg7AsBEHoNgZARBsAYGYKxBo0A8RWaOKsRgohGBEFoGgQ0amZAaYkDpmWemDOeAAIKeG8DREALgFbgE0wAfSIOkVaIwhDJEXNNSGAAvSAtgHoAHo1DIAAAQAAoADqERoCBckGV9qZXnbKGQAAbjKzVuQ6wOsXHWAASjKxFyI40quiFoAAaX7CVnAyhuSVYm4ZnQ4MUgCDK7YSALgyuk1EGgJwMhBsAGFDA+GKKIIrHnWtzfsRgdQkoyvuCIDYc4M3bvRwmPFxQD0ZZgFS1YTLo5pr7bwBN7qH23CKDQDIWwy0kvQFEJETwpmAfZbGOBUAn36JmAsKIJLZ2AbiGpij4aeEaSY5AJES48MkuIxOpoLLw0SDKEwuDhLhgiDiGgHuDnuOocSzAOIcQq00BE5EIDq6rPFBC8kNDmI0NifjgCEfUyxtyCgklwgIgyQCs+dnDT0QMvFzswV4EZXPJ7Rq41yAAcZ3cvyFxzITgDgMti9R3APAWF7wY4hwgBwkhpDyCS09Zaf36fi7uFbmHaA7BB88CHtLYe3evm9wl2rogLiiGgHD5EJuI9k590tSIq04fDB849f7rvGdW7QNEJLhNHqvEr9NMAcgnByECwoK3cgteQHSMMWHM5hjsGWqUXPIAuu/jFOTurSX2+eCS94WGThE/DXAK39ve5O/54S0L9IYAHriCSzOMA6QIiN4Z4rkAx3TuiDKwABWMFp+/i5T9yDgHAO/y1Xq0FnGV4wMg0AwAzsEgystMR9hh38iARsNto8gYisLg8B0gZAMhZw8AjAb88BIhoB2AAA/LA9gTQa/KcW/B/J/IcSAUQPcCQd/SA6AiwJGIrfAvA7AzQVqdaMQMrQ7DbdLGguAKAmceguAhA7vQmHAgQfgmAhghAyIEQ2wHAkAdXbfSHIgOQZIc/cPPedgUQKsegXQ+gNAZAWgQwkgLgDzdgcZZAbQogQw8wqfAvKg2gdIWwFfaacwrANAcgNAdgXQhzZhDwo2bA8ZVYGwcJTAIsNeOwhLBwpwpLMQOQOrcQFwxQUmZApw2/AmZQHAiLVqUmFIZqSreIRIWwCrTqQbQzYwbbRGSIQwCwBrN5crYwXaXbTwLAYwGuMrYQSQJLegJLcrSILono5AfrSIxQIgaAH/AA5fXPDcBwK3dnLo7grPb7PfP7dQt3GYrcJQhAeYpLRY/XQ3OXU6aYuwWYrYkAHYvYmQNY4aDYuYx6XYigrPALILRI44zcK3OPAwQwIPMAEbL/JI7IAoDYgQDYxQlPRQAELo4fBIa4y/CLc4OwTQeEgaMrAAIQej2yRIRNsEaw53UyxJRIAFU+wod4cytwZ3BNBUTkCnAhsEhIAABHX7KkmkoYOQMrfaWwaAB7KmWcQguwSANTXYIQQ7IgYoIU1oK/MUiU8k4YZHK/dLAXUXQ7RUwnbbQGGoooEU1U1wB7IwZA2wWgGkwgqcCwB7FQhrCkk0zaaHR6E0gXCg14q/fQFacQRrSgzQUmDnMU+QQ0HbZaU/SUwzeGMQAcaPTQWIacWGF3FIAwGAIgNE84dIQwGMuM4gTguwDbdIKowwUXWMtAeMzg+QQ3CvfMwsrTIgK4IQMs9M4zeIvcc4AcGWTQGshMx7YGastMtsi0srHQVwIvBs/sCQFsrs80zaMrYkiwGQeHTQcGCwHwGXdgTwMchrdwCQSAAgoQSGOffs2/Q7ZaaQZIWc9wdUpHCwY8+/FIs8rUkACklch7dczc28k8tc84J8u/OwdadvMrFICIQGXczQNcpAkg8LQC0QYCvU84RHMCiCwk2IGCmQW/OCn83vFMhCpC2IB84oQU6HQ0ICxCiczC9wVwcU6HTQHQIgQwKcSUnQSAM7RvWi+i90vcMrTqaihQIQHQIXWgL4ucckykoQIcCQYgbvTQLrdIaWOEIQcSyShreSGSkmBrWUdXdXIAA=="}
enctp: 1
encpw: 46e6d22f02dc33fa33d52333a819c76b96f768dd63af6495f67887388ed4d58206448e1532e833ca98fd44cd75f1918643848f918e17b7fb4a32ce320436291bb2959257f9ecbe64eed37fcc8387d2796f08e1184f279b524b81f4a96a882916e2980b2df6a1b91fb03b229f34c85b1e4a6b951f4ccad5db7b7c3a3070d8585e
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


hheader='''\
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
cache-control: max-age=0
content-length: 5675
content-type: application/x-www-form-urlencoded
origin: https://nid.naver.com
referer: https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36\
'''.splitlines()

rhead=[]

for head in hheader:
    head= head.replace(" ", "")
    rhead.append(head)
#print(rhead)

rrhead={}
for head in rhead:
    key,value=head.split(":",1)
    rrhead[key]=value

sess=requests.Session()
res=sess.post(url,data=data)
time.sleep(3)
html=res.text
print(html)
# soup=BeautifulSoup(html,'html.parser')
# print(html)
# for tag in soup.select('.private.user_name'):
#     print(tag.text.strip())
# results=soup.select_one("span.blind")
# print(results.text)

# results=soup.select_one("div.private > span.user strong")
# #print(results.text)