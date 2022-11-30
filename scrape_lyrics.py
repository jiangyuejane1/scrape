#!/usr/bin/env python
# coding: utf-8

# In[89]:


import requests


# In[90]:


from bs4 import BeautifulSoup


# In[91]:


def scrape_lyrics(url):
    response = requests.get(url)
    html_string = response.text
    document = BeautifulSoup(html_string, "html.parser")
    lyrics = document.find("div", attrs={"class": "col-xs-12 col-lg-8 text-center"}).text.replace('\n','')
    lyrics = lyrics.split('\r')
    return lyrics[1].split('Submit')[0]


# In[92]:


def scrape_artist(url):
    response = requests.get(url)
    html_string = response.text
    document = BeautifulSoup(html_string, "html.parser")
    artist = document.find("div", attrs={"class": "lyricsh"}).text.replace('\n','')
    return artist[:-7]


# In[93]:


def scrape_title(url):
    response = requests.get(url)
    html_string = response.text
    document = BeautifulSoup(html_string, "html.parser")
    title = document.find("h1").text
    title = title.split('"')
    return title[-2]


# In[94]:


scrape_url = ["https://www.azlyrics.com/lyrics/taylorswift/timmcgraw.html",
              "https://www.azlyrics.com/lyrics/taylorswift/picturetoburn.html",
              "https://www.azlyrics.com/lyrics/taylorswift/teardropsonmyguitar.html"]


# In[95]:


import pandas as pd


# In[96]:


dic_scrape = {}
artist = []
title = []
lyrics = []
for url in scrape_url:
    artist.append(scrape_artist(url))
    title.append(scrape_title(url))
    lyrics.append(scrape_lyrics(url))


# In[97]:


dic_scrape['artist'] = artist
dic_scrape['title'] = title
dic_scrape['lyrics'] = lyrics


# In[98]:


pd.DataFrame(dic_scrape)

