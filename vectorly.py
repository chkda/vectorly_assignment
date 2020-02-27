#!/usr/bin/env python
# coding: utf-8

# In[19]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[135]:


def getTextOverlay(image):
    output = np.zeros(image.shape,dtype="uint8") 
    output[image[:,:,2] < 20] = 128
    struct_elem = np.ones((7,7),dtype="uint8")
    output = cv2.morphologyEx(output,cv2.MORPH_OPEN,struct_elem)
    _,output = cv2.threshold(output,127,255,cv2.THRESH_BINARY_INV)
    return output
    


# In[136]:


if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)


# In[137]:





# In[138]:





# In[132]:





# In[126]:





# In[ ]:




