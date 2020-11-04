import pandas as pd
import re
import requests
from googlesearch import search

df = pd.read_csv('PDM.csv')
df.head()

df['MIDDLE'].isnull().sum()
df['MIDDLE'].fillna('', inplace=True)

df['PHONE1'] = df.PHONE1.astype('str')
df['new'] = df['FIRST'] + " " + df['MIDDLE'] + " " + df['LAST'] + " " + df['PHONE1']

# x = 0
# for i in df['PHONE1']:
#     i = str(i)
#     df['new'][x] = df['new'][x] + " " + i
#     x = x + 1

lists = []


def get_urls(tag, n, language):
    for url in search(tag, stop=n, lang=language):
        lists.append(url)

    return lists


for i in df['new']:
    strng = i
    get_urls(strng, 1, 'en')


def custom_preprocessor(text):
    """
    Make text lowercase, remove text in square brackets,remove links,remove special characters
    and remove words containing numbers.
    """
    text = text.lower()
    text = re.sub('\[.*?] ', '', text)
    text = re.sub("\\W", " ", text)  # remove special chars
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    # text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('[a-z]+', '', text)

    return text


present = []
source = []
print(lists)
x = 0
# k = df['PHONE1']
for i in df['PHONE1']:
    f = requests.get(lists[x])
    print(lists[x])
    x = x + 1
    z = f.text
    print(i)
    i = str(i)
    a = custom_preprocessor(z)
    a = a.replace(" ", "")
    el = a.find(i)
    if el == -1:
        present.append('False')
        source.append(' ')
        print('false')

    else:
        present.append('True')
        source.append(lists[x])

        print('True')

print(present)
print(source)
