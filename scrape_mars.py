#!/usr/bin/env python
# coding: utf-8

# In[89]:


from bs4 import BeautifulSoup
import requests
import os
import pprint
import time


# In[91]:



# In[92]:


from splinter import Browser


# In[93]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# In[21]:


#url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
#response = requests.get(url)


# In[88]:


#soup = BeautifulSoup(response.text, 'lxml')
#print(soup.prettify())


# In[94]:


url ="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)
time.sleep(2)


# In[95]:


html=browser.html
soup=BeautifulSoup(html,'html.parser')
print(soup)


# In[97]:


#date=soup.find_all(class_='list_date')
#date


# In[98]:


news_title=soup.find_all('div',class_='content_title')[0].text
news_title


# In[99]:


news_p =soup.find_all('div',class_='article_teaser_body')[0].text
news_p


# ## PL Mars Space Images - Featured Image

# In[37]:


url ="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[42]:


html=browser.html
soup=BeautifulSoup(html,'html.parser')
print(soup)


# In[46]:


url=soup.find_all('a',class_='fancybox')[0]['data-fancybox-href']


# In[51]:


featured_image_url="https://www.jpl.nasa.gov"+url


# In[52]:


featured_image_url


# ## Mars Weather

# In[55]:


url="https://twitter.com/marswxreport?lang=en"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())


# In[60]:


mars_weather=soup.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
mars_weather


# ## Mars Facts

# In[61]:


import pandas as pd


# In[66]:


url="http://space-facts.com/mars/"


# In[67]:


tables=pd.read_html(url)
tables


# In[70]:


df=tables[0]
df.columns=['Parameter', 'Data']
df.head()


# ## Mars Hemispheres 

# In[71]:


url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


# In[78]:


img_url=soup.find_all('a',class_='itemLink product-item')
img_url


# In[82]:


access=[]

for url in img_url:
    link="https://astrogeology.usgs.gov"+url['href']
    access.append(link)
    
print(access)

image_link=[]

for x in access:
    response = requests.get(x)
    soup = BeautifulSoup(response.text, 'lxml')
    link=soup.find_all('a')[41]['href']
    image_link.append(link)
    
print(image_link)


# In[84]:

url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


titles=soup.find_all('h3')
titles


# In[86]:


title_list=[]

for title in titles:
    title_name=title.text.replace('Enhanced', '')
    title_list.append(title_name)
    
print(title_list)


# In[104]:


hemisphere_image_urls=[]
for x in range(4):
    dict={"title":title_list[x],"img_url":image_link[x]}
    hemisphere_image_urls.append(dict)
    
hemisphere_image_urls

browser.quit()

# In[ ]:
def scrape():
    dictionary={"news_title":news_title,
                "news_p":news_p,
                "featured_image_url":featured_image_url,
                "mars_weather":mars_weather,
                "hemisphere_image_urls":hemisphere_image_urls}
    return dictionary





