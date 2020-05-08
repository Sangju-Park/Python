#!/usr/bin/env python
# coding: utf-8

# In[27]:


import urllib.request as reg
import requests as rts


# In[26]:


url="https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=유현주%20프로"
rts..encoding('utf8')
r=reg.urlopen(url)


# In[17]:


#f=open('daumnet.html','w',encoding='utf8')
#f.write(r.read().decode('utf-8'))
#f.close


# In[4]:


data=r.read().decode('utf8')


# In[5]:


import re

urls=re.findall('https://[./-_\w]+\.jpg',data)


# In[6]:


for url in urls :
    index=url.rfind('/')
    f=open(url[index+1:],'wb')
    res=reg.urlopen(url)
    f.write(res.read())
    f.close

    
    


# In[7]:


type(url)


# In[ ]:




