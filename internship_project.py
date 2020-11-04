import logging
import re

import pandas as pd
import requests
from googlesearch import search

logging.getLogger('scrapy').propagate = False

df = pd.read_csv('PDM.csv')
df['MIDDLE'].isnull().sum()
df['MIDDLE'].fillna('', inplace=True)
#
# for x in df['PHONE1']:
#     print(x)

df['PHONE1'] = df.PHONE1.astype('str')
df['new'] = df['FIRST'] + " " + df['MIDDLE'] + " " + df['LAST'] + " " + df['PHONE1']
print(df['new'])

lists = []


def get_urls(tag, n, language):
    for url in search(tag, stop=n, lang=language):
        lists.append(url)
        return lists


for i in df['new']:
    strng = i
    strng = strng.lower()
    get_urls(strng, 4, 'en')

print(lists)


def custom_preprocessor(text):
    """
    Make text lowercase, remove text in square brackets,remove links,remove special characters
    and remove words containing numbers.
    """
    text = text.lower()
    text = re.sub('\[.*?]', '', text)
    text = re.sub("\\W", " ", text)  # remove special chars
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    # text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[a-z]+', '', text)

    return text


x = 0
for j in df['PHONE1']:

    strng = " "
    for i in range(4):
        link = lists[x]
        x = x + 1
        f = requests.get(link)
        z = f.text
        a = custom_preprocessor(z)
        a = a.replace(" ", "")
        strng = strng + a
        j = str(j)
        el = strng.find(j)
        if el == -1:
            print('false ' + lists[x])
        else:
            print('true ' + lists[x])
        print(x)
