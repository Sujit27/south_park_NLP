#!/usr/bin/env python
# coding: utf-8

# **This notebook creates transcripts from all episodes of SouthPark till Season 22**

# In[23]:


from bs4 import BeautifulSoup
import requests
import os


# In[24]:


def create_season_url(season_url_part,season_number='Season_One'):
    season_url_complete = season_url_part + season_number
    return season_url_complete


# In[25]:


def create_episode_url(episode_url_part,episode_name=None):
    episode_url_complete = episode_url_part + episode_name + "/Script"
    return episode_url_complete


# In[26]:


def list_all_episodes_of_a_season(season_url_complete):
    source = requests.get(season_url_complete).text
    soup = BeautifulSoup(source,'lxml')
    
    body = soup.body
    wiki = body.find('div',class_='WikiaSiteWrapper')
    wiki = wiki.section.find('div', class_="WikiaPageContentWrapper")
    wiki = wiki.find('article',class_='WikiaMainContent')
    wiki = wiki.find('div',class_='WikiaMainContentContainer')
    wiki = wiki.find('div',class_='WikiaArticle')
    wiki = wiki.find('div',id='mw-content-text')
    wiki = wiki.findAll('div')[6]
    wiki = wiki.find('div',id='gallery-0')
    episodes = []
    for item in wiki.findAll('div',class_="wikia-gallery-item"):
        title = item.find('div',class_="lightbox-caption").a.text
        episodes.append(title)
        
    return episodes


# In[27]:


def create_transcript_of_an_episode(episode_url_complete):
    source = requests.get(episode_url_complete).text
    soup = BeautifulSoup(source,'lxml')
    
    body = soup.body
    wiki = body.find('div',class_='WikiaSiteWrapper')
    wiki = wiki.section.find('article')
    wiki = wiki.find('div',class_='WikiaMainContentContainer')
    wiki = wiki.find('div',class_='WikiaArticle')
    wiki = wiki.find('div',id='mw-content-text')
    table = wiki.findAll('table')[1]
    transcript = []
    for entry in table.findAll('tr'):
        transcript.append(entry.text)
        
    return transcript


# In[28]:


def save_transcript(output_directory,episode_name,episode_transcript):
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    file_name = episode_name + ".txt"
    output_file = os.path.join(output_directory,file_name)
    with open(output_file,'w') as f:
        for line in episode_transcript:
            f.write('%s\n' %line)


# In[29]:


season_url_part = 'https://southpark.fandom.com/wiki/Portal:Scripts/'
episode_url_part = 'https://southpark.fandom.com/wiki/'


# **List of seasons**

# In[30]:


season_numbers = ['Season_One','Season_Two','Season_Three','Season_Four','Season_Five','Season_Six','Season_Seven','Season_Eight',
                 'Season_Nine','Season_Ten','Season_Eleven','Season_Twelve','Season_Thirteen','Season_Fourteen','Season_Fifteen',
                  'Season_Sixteen','Season_Seventeen','Season_Eighteen','Season_Nineteen','Season_Twenty','Season_Twenty-One',
                 'Season_Twenty-Two']


# In[31]:


output_directory = "south_park_episode_transcripts"


# **Create Transcripts**

# In[34]:


for season_number in season_numbers:
    
    season_url_complete = create_season_url(season_url_part,season_number)
    try:
        episodes = list_all_episodes_of_a_season(season_url_complete)
    except:
        print("No season with number ",season_number)
        
    for episode in episodes:
        episode_url_complete = create_episode_url(episode_url_part,episode)
        try:
            transcript = create_transcript_of_an_episode(episode_url_complete)
        except:
            print("No episode with name ", episode)
        
        save_transcript(output_directory,episode,transcript)
        
        print("Saved episode ", episode)
        
    print("{} completed".format(season_number))    
    




