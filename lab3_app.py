#!/usr/bin/env python
# coding: utf-8

# # Calculating similarity between two sentences using wordnet.

# In[1]:


import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('all')


# In[54]:


from nltk import word_tokenize
import statistics
import streamlit as st

# In[55]:
st.title("Sentence Similarity Calculator")
form = st.form(key='my-form')
sent1 = form.text_input('Enter Sentence 1')
sent2 = form.text_input('Enter Sentence 2')
submit = form.form_submit_button('Calculate Similarity')



def calc_similarity(sen1,sen2):
  s1=word_tokenize(sen1)
  s2=word_tokenize(sen2)
  l1=[]#To store synsets of Sentence 1 words
  l2=[]#To store synsets of Sentence 2 words
  sim_score=[]#To store similarity score of each word between 2 sentences
  for i in s1:
    l1.append(wordnet.synsets(i)[0])
  for i in s2:
    l2.append(wordnet.synsets(i)[0])
  for i in l1:
    for j in l2:
      sim_score.append(round(i.wup_similarity(j),3))#Calculating the similarity score of each word between 2 sentences
      
  
  
  #print(f"\nSimilarity Score Of the words between each sentences = {sim_score}\n")
  #print(f"Mean Similarity Score between {sen1} and {sen2} = {statistics.mean(sim_score)}\n")
  #print(f"Percentage Similarity Score = {statistics.mean(sim_score):.2%}")
    
  
  return sim_score, statistics.mean(sim_score)

# In[57]:


#sen1 = input("Enter Sentence 1 : ")
#sen2 = input("Enter Sentence 2 : ")
#calc_similarity(sen1,sen2)


# In[1]:

    
if submit:
    similarity_score, mean_similarity_score=calc_similarity(sent1,sent2)    
    #st.write(calc_similarity(sent1,sent2))
    st.write(f"\nSimilarity Score Of the words between each sentences = **{similarity_score}**\n")
    st.write(f"Mean Similarity Score between **'{sent1}'** and **'{sent2}'** = **{mean_similarity_score}**\n")
    st.write(f"Percentage Similarity Score = **{mean_similarity_score:.2%}**")



# In[2]:





# In[ ]:




