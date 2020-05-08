#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import cv2
import matplotlib.pyplot as plt
import numpy as np
img_basic = cv2.imread('rhj.jpg', cv2.IMREAD_UNCHANGED)
mm=cv2.cvtColor(img_basic, cv2.COLOR_BGR2RGB)
plt.imshow(mm)


# In[2]:


type(img_basic)


# In[3]:


img_basic = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
rhj=plt.imshow(cv2.cvtColor(img_basic, cv2.COLOR_GRAY2RGB))
plt.show()


# In[4]:



import cv2
import matplotlib.pyplot as plt

im1=cv2.imread("rhj.jpg",cv2.IMREAD_COLOR)
plt.imshow(im1)


# In[ ]:


cv2.imshow("RHJ",im1)
cv2.waitKey(0)
cv2.imwrite('RHJ.jpg',im1)


# In[ ]:


cv2.imshow('',im1)
cv2.waitKey(0)
cv2.imwrite('RHJ.jpg',im1)


# In[ ]:


cv2.destroyAllWindows()


# In[ ]:


import cv2
import matplotlib.pyplot as plt
import time

image = cv2.imread('rhj.jpg')

start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
image[0:100, 0:100] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()


# In[ ]:


import cv2
import matplotlib.pyplot as plt

imge=cv2.imread('rhj.jpg')

roi=imge[100:300,200:400 ]
imge[0:200,0:200]=roi

plt.imshow(cv2.cvtColor(imge, cv2.COLOR_BGR2RGB))
plt.show()


# In[ ]:


import cv2
import matplotlib.pyplot as plt
plt.figure(figsize=(12*3,3*3))
mm=cv2.imread('rhj2.jpg')
#mm[:,:,0]=1
plt.imshow(cv2.cvtColor(mm,cv2.COLOR_BGR2RGB))
plt.show()


# In[ ]:


np.shape(mm)


# In[ ]:


mm.size


# In[ ]:


818*647*3-mm.size


# In[ ]:


import numpy as np
arr=np.arange(24).reshape(4,3,2)
arr


# In[ ]:


np.sum(arr,axis=0)


# In[ ]:




