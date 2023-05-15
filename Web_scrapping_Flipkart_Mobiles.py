#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests


# In[2]:


url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# In[3]:


driver = webdriver.Chrome(executable_path=r'C:\Users\pavan\Desktop\business analytics\chromedriver.exe')
driver.implicitly_wait(10)
driver.get(url)


# In[4]:


soup= BeautifulSoup(driver.page_source,'html.parser')


# # Next_Page_links

# In[8]:


link=soup.find_all('a',{'class':'ge-49M'})


# In[14]:


next_page=[]
for i in link:
    next_page.append('https://www.flipkart.com'+i.get('href'))
next_page


# # Mobile_Name

# In[15]:


Mobile_name=[]
for i in next_page:
    driver.get(i)
    m_link=soup.find_all('div',{'class':'_3pLy-c row'})
    for j in m_link:
        name=j.find_all('div',{'class':'_4rR01T'})
        for k in name:
            Mobile_name.append(k.text)
Mobile_name


# In[16]:


len(Mobile_name)


# # Rating

# In[17]:


rating=[]
for i in next_page:
    driver.get(i)
    links=soup.find_all('div',{'class':'gUuXy-'})
    for j in links:
        rating.append(j.text)
rating        


# In[19]:


len(rating)


# # Specification

# In[18]:


specification=[]
for i in next_page:
    driver.get(i)
    links=soup.find_all('div',{'class':'fMghEO'})
    for j in links:
        specification.append(j.text)
specification


# In[20]:


len(specification)


# # Price

# In[21]:


price=[]
for i in next_page:
    driver.get(i)
    links=soup.find_all('div',{'class':'_30jeq3 _1_WHN1'})
    for j in links:
        price.append(j.text)
price


# In[22]:


len(price)


# # Mobile_links

# In[25]:


mobile_links=[]
for i in next_page:
    driver.get(i)
    links=soup.find_all('a',{'class':'_1fQZEK'})
    for j in links:
        mobile_links.append(j.get('href'))
mobile_links


# In[26]:


len(mobile_links)


# # CSV Files

# In[27]:


dataframe1=pd.DataFrame(Mobile_name)
dataframe1


# In[30]:


dataframe2=pd.DataFrame(rating)
dataframe2


# In[31]:


dataframe3=pd.DataFrame(specification)
dataframe3


# In[32]:


dataframe4=pd.DataFrame(price)
dataframe4


# In[33]:


dataframe5=pd.DataFrame(mobile_links)
dataframe5


# In[34]:


dataframe1.to_csv('df1.csv')


# In[35]:


dataframe2.to_csv('df2.csv')


# In[36]:


dataframe3.to_csv('df3.csv')


# In[37]:


dataframe4.to_csv('df4.csv')


# In[38]:


dataframe5.to_csv('df5.csv')

