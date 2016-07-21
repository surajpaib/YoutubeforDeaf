import pandas as pd
import csv
import subprocess

ifile=open("..\Python Code\wordlist1.csv","r")
wordloop=csv.reader(ifile)



searchwords=[]

for row in wordloop:
    t=str(row).strip('[]')
    k=t[1:-1]
    searchwords.append(k)

    print str('/^[' + str(k[0].upper()) + str(k[0]) + ']' + str(k[1:-1]) +'['+str(k[-1])+']')


def woi():
    return searchwords




