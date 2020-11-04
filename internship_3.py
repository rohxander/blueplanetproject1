#import libraries
import logging
import os
import pandas as pd
import re
from googlesearch import search
import urllib
import requests
 
 #read the csv file
df=pd.read_csv('PDM.csv')
df.head()

#check whether any value is missing or not
df['MIDDLE'].isnull().sum()
df['MIDDLE'].fillna('',inplace=True)


# concatenate  First middle and last name with the phone number and 
df['new']=df['FIRST']+" "+df['MIDDLE']+" "+df['LAST']
df['PHONE1']=df.PHONE1.astype('str')
df['new']=df['FIRST']+" "+df['MIDDLE']+" "+df['LAST']+" "+df['PHONE1']


# obltain the urls on the basis of first middle ,last name and phone number
list=[]
def get_urls(tag, n, language):
    for url in search(tag, stop=n, lang=language):
        list.append(url)
    
    return list
for i in df['new']:
    strng=i
    get_urls(strng,1,'en')
list

# Extract all the numbers from that website The function below will extract all the numbers only
def custom_preprocessor(text):
    '''
    Make text lowercase, remove text in square brackets,remove links,remove special characters
    and remove words containing numbers.
    '''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) # remove special chars
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    #text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[a-z]+', '', text)
    
    
    return text

# one by one take all the urls from the list and match the number with the phone number of Doctor
x=0
present=[]
source=[]
for i in df['PHONE1']:
    f = requests.get(list[x])
    print(list[x])
    x=x+1
    z=f.text
    print(i)
    i=str(i)
    a=custom_preprocessor(z)
    a=a.replace(" ","")
    el=a.find(i)
    if(el== -1):
        present.append('False')
        source.append(' ')
        #print('false')

    else:
        present.append('True')
        source.append(list[x])
        #print('True')

df[present]=present
df[source]=source
