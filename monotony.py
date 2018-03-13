'''
Created on Mar 13, 2018

Updated: 18:34 Mar 13, 2018

@author: Strassboom

@name monotony.py

Latest Python version supported: 3.6
@note: Libraries used: psutil, threading, webbrowser
@note: Libraries to download: psutil
'''

import random
import psutil
import threading
import webbrowser

if __name__ == '__main__':
    
    def printit():
        #Change the First arg below to change the repeat delay by x seconds
        threading.Timer(5.0, printit).start()
        progname = "Acrobat.exe"
        for p in psutil.process_iter():
            if p.name() == progname:
                p.kill()
                
printit()