import urllib.request as fetchFrom
from bs4 import BeautifulSoup as include

url = input("Enter the URL: ")

websiteResponse = fetchFrom.urlopen(url)
htmlCode = websiteResponse.read()

s = include(htmlCode,'html.parser')
s.body.append(include('<script src="dani"></script>','html.parser'))
              
htmlFile = open('../../../index.html','w',encoding='utf-8')
htmlFile.write(str(s))
htmlFile.close()

"""import os

os.system('cmd /k "cd/ & cd users\dani\desktop & rename index.html dani.html"')
"""
