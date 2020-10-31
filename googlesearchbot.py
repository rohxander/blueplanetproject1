# importing pandas as pd
import pandas as pd

# read an excel file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_excel("sample_record_1.xlsx"))

# show the dataframe
print(df)



























# import requests, sys, webbrowser, bs4
# import pandas as pd
# import numpy
#
# f = pd.read_csv("uszips.csv")
# f = f.drop('lat',axis=2)
# coloumns_to_keep = ['zip', 'city', 'state_name']
# new_f = f[coloumns_to_keep]
# res = request.get('https://google.com/search?q='+''.join(sys.argv[1:]))
# res.raise_for_status()
#
# soup = bs4.BeautifulSoup(res.text, "html.parser")
#
# linkElements = soup.select('.r a')
# linkToOpen = min(5, len(linkElements))
# for i in range(linkToOpen):
# ffffff