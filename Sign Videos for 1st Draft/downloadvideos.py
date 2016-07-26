import pandas as pd
import csv
import subprocess

## Retrieves the list of words from the video
ifile=open("..\Python Code\wordlist.csv","r")
wordloop=csv.reader(ifile)



searchwords=[]


## Saves the words to a list
for row in wordloop:
    t=str(row).strip('[]')
    k=t[1:-1]
    command="youtube-dl -o '%(title)s' ytuser:isldictionary --match-title "+str(k)
    subprocess.call(command.split())
    searchwords.append(k)





def woi():
    return searchwords




