import urllib.request as fetchFrom, os
from bs4 import BeautifulSoup as include

url = input("Enter the URL: ")
if url=='':
    print("Invalid URL...")
else:
    websiteResponse = fetchFrom.urlopen(url)
    htmlCode = websiteResponse.read()

    s = include(htmlCode,'html.parser')
    #s.body.append(include('<script src="dani"></script>','html.parser'))

    os.system('cmd /c "cordova create fname com.demo.ddr aname & cd fname & cordova platform add android"')
    
    htmlFile = open('fname\www\index.html','w',encoding='utf-8')
    htmlFile.write(str(s))
    htmlFile.close()


    os.system('cmd /c "cd fname & cordova build android"')
    os.system('cmd /c "cd fname/platforms/android/app/build/outputs/apk/debug & start ."')


