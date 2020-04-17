#!/usr/bin/env python
# coding: utf-8

# In[262]:


import os
from load import loadPrepareData
import random
from nltk.tag import pos_tag
import re
import string


# In[264]:


def is_character_name(sent):
#     x = sent.split(" ")[1:]
#     punctuation = ['.','?','!','-',',','']
    last_char = sent[-2]
    size = len(sent)
    if (last_char not in string.punctuation) and (last_char !=" ") and size < 20:
        return True
    else:
        return False


# In[266]:


def remove_non_dialogue(transcript):
    transcript_mod = []
    for index,sent in enumerate(transcript):
        if sent == "\n" or sent == " \n":
            continue
        if (is_character_name(sent)) and (index+1 < len(transcript)):
            transcript_mod.append(transcript[index+1])
#             print(sent)
            
    return transcript_mod


# In[268]:


def remove_brackets(transcript):
    new_transcript = []
    for sent in transcript:
        sent = re.sub(r'\[.*\]', '', sent)
        sent = re.sub(r'\(.*\)', '', sent)
        new_transcript.append(sent)
        
    return new_transcript


# In[270]:


def open_transcript(transcript_file):
    with open(transcript_file) as f:
        transcript = f.readlines()
    
    return transcript


# In[271]:


movie_corpus = "data/movie_subtitles.txt"


# In[272]:


data_dir = "south_park_episode_transcripts"
transcript_files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
# print("There are {} transcript files in the directory".format(len(transcript_files)))
combined_clean_transcript = []
for transcript_file in transcript_files:
    transcript = open_transcript(os.path.join(data_dir,transcript_file))
#     transcript = clean_transcript(transcript)
    transcript = [line for line in transcript if line != '\n'][1:]
    transcript = remove_brackets(transcript)
    transcript = remove_non_dialogue(transcript)
    combined_clean_transcript.append(transcript)
#     break
    
    
combined_clean_transcript = [sent for chapter in combined_clean_transcript for sent in chapter] # flatten the list and remove first space
combined_clean_transcript = [sent for sent in combined_clean_transcript if sent !="\n" and sent !=" \n"]
if len(combined_clean_transcript)%2 == 1:
    combined_clean_transcript.pop()


# In[273]:


len(combined_clean_transcript)


# In[274]:


# # print(combined_clean_transcript)
# for item in combined_clean_transcript:
#     print(item)


# In[275]:


len(combined_clean_transcript)


# In[277]:


with open(os.path.join('data',"south_park_subtitles.txt"),'w') as f:
    for sent in combined_clean_transcript:
        f.write('%s' %sent)


# In[278]:


corpus = 'data/south_park_subtitles.txt'


# In[279]:


voc, pairs = loadPrepareData(corpus)


# In[280]:


rand_pairs = random.sample(pairs,5)
print("Random pairs of dialogues")
for item in rand_pairs:
    print(item)


# In[281]:


#print(voc.n_words)


# In[ ]:




