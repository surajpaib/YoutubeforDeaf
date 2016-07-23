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
    searchwords.append(k)





def woi():
    return searchwords




