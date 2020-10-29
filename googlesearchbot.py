import requests, sys, webbrowser, bs4

filename = "doctorlist.csv"
headers = "Name,Type,Gender,Address1,City,PINCODE,PhoneNumber\n"
f = open(filename,"w")
f.write(headers)
f.close()
# res = request.get('https://google.com/search?q='+''.join(sys.argv[1:]))
# res.raise_for_status()
#
# soup = bs4.BeautifulSoup(res.text, "html.parser")
#
# linkElements = soup.select('.r a')
# linkToOpen = min(5, len(linkElements))
# for i in range(linkToOpen):
# hello