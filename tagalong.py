'''
Created on Feb 6, 2018

Updated: 18:38 Mar 13, 2018
@author: Strassboom

Latest Python version supported: 3.6
@note: Libraries used: psutil, threading, webbrowser
@note: Libraries to download: psutil
'''

import random
import psutil
import threading
import webbrowser

if __name__ == '__main__':
    

    def getweb():
        netting = []
        if len(netting) == 1:
            return netting[0]
        elif len(netting) > 1:
            chosen = random.randint(0, len(netting))
            return netting[chosen]
        else:
            return 'https://www.python.org/'
        
    def catcher():
        # Change first argument to set repeat delay to x seconds
        threading.Timer(5.0, catcher).start()
        liner = []
        progname = "firefox.exe"
        for p in psutil.process_iter():
            liner.append(p.name())
        if progname in liner:
            webbrowser.open(getweb())
        
catcher()