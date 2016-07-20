import pandas as pd
import csv
import subprocess

ifile=open("F:\DISQ Files\YoutubeforDeaf\Python Code\wordlist1.csv","r")
wordloop=csv.reader(ifile)


for row in wordloop:
    t=str(row).strip('[]')
    k=t[1:-1]

    command = "youtube-dl -o '%(title)s' --match-title "+k+" ytuser:isldictionary"
    subprocess.call(command.split(),shell=True)




