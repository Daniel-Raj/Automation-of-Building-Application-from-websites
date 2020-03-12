# Needed packages

from tkinter import *
from tkinter import ttk

import urllib.request as fetchFrom, os
from bs4 import BeautifulSoup as include

### Automation function Starts here
def distatus():
    try:
        url = data.get()
        appname = appdata.get()
        
        if url ==  '' and appname ==  '':
            status1.set("Invalid URL...")
        else:
            
            websiteResponse = fetchFrom.urlopen(url)
            htmlCode = websiteResponse.read()
            s = include(htmlCode,'html.parser')
            fder = appname + 'folder'      
            os.system('cmd /c "cordova create '+ fder +' com.demo.ddr ' + appname + ' & cd '+ fder +' & cordova platform add android"')
            status1.set('#1 - project created!')
           
            htmlFile = open(fder+'\www\index.html','w',encoding = 'utf-8')
            htmlFile.write(str(s))
            htmlFile.close()
         
            os.system('cmd /c "cd '+ fder + ' & cordova build android"')
            status2.set('#2 - App created!')
            os.system('cmd /c "cd '+ fder +'/platforms/android/app/build/outputs/apk/debug & start ."')
    except:
        status1.set('#1 - Error!')
        status2.set('#2 - Check the above fields or your internet connection')
### Automation function ends here      
        
###GUI starts here
window = Tk()
window.title('Build ur Apk here! ')
window.columnconfigure(0,weight = 1)


status1 = StringVar()
status2 = StringVar()
data = StringVar()
appdata = StringVar()


ttk.Label(window,text = 'URL').grid(sticky = 'w')
ttk.Entry(window,textvariable = data,width = 50).grid(padx = 10)
ttk.Label(window,text = 'App Name').grid(sticky = 'w')
ttk.Entry(window,textvariable = appdata,width = 50).grid()
ttk.Label(window,text = '').grid()
ttk.Button(window,text = 'BUILD',command = distatus).grid()
ttk.Label(window,text = '').grid()
ttk.Label(window,textvariable = status1).grid(sticky = 'w')
ttk.Label(window,textvariable = status2).grid(sticky = 'w')

###GUI ends here
