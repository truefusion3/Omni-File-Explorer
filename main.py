# Import
import os
import tkinter as tk
import random as rnd
import getpass
import logging as log

# Prerequisites
log.basicConfig(filename='omni.log', level=log.INFO) # starts logger
logger = log.getLogger(__name__)
logger.info("Log Initialised")
user = getpass.getuser() # user = sravi
logger.info("User Selected")
window = tk.Tk()

# Set directories
root = "/" # root folder
logger.info("Root defined")
downloads = "/Users/"+ user +"/Downloads" # downloads folder
logger.info("Downloads defined")
documents = "/Users/"+ user +"/Documents" # documents folder
logger.info("Documents defined")
desktop = "/Users/"+ user +"/Desktop" # desktop folder
logger.info("Desktop defined")
library = "/Users/"+ user +"/Library" # user library folder
logger.info("Library defined")

setroot = "" # root folder for depth first search
dirList = [] # List of directories to be set

def exit():
    quit()

def initWindow():
    window.title("Omni File Explorer")
    window.minsize(500, 500)
    window.maxsize(1000, 1000)
    window.geometry("1000x700+375+100")
    tk.Label(window, text="Test").pack()
    window.lift()
    window.attributes('-topmost', True)
    window.focus_force()
    tk.Button(window, text="search", command=search).pack()
    window.after(100, lambda: window.attributes('-topmost', False))

def search():
    for item in dirList:
        print(len(dirList))
        tk.Label(window, text=item).pack()
        window.config(text="testing testing 1 2 3")

def main():
    dirList = os.listdir()
    print(dirList)
    initWindow()
    window.mainloop()
    

if __name__ == '__main__':
    main()