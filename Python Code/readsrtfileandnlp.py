import nltk
import pysrt
from nltk import word_tokenize
from catergorize import cattags
import pandas as pd


## Read srt file
sub=pysrt.open("..\Python Code\subtitle.srt")
starttime=[]
endtime=[]
text=[]
for i in range(len(sub)):
    ## Store metadata from the srt files
    case=sub[i]
    text.append(case.text)
    starttime.append(case.start)
    endtime.append(case.end)

## Get all the Part of Speech tags
verbset,verbpos,nounset,nounpos,pronset,pronpos,adjecset,adjpos,advset,advpos,adpset,adppos,conjset,conjpos,detset,detpos,numset,numpos,prtset,prtpos,xset,xpos=cattags(text)
wordlist=nounset+verbset+adjecset
wordpos=nounpos+verbpos+adjpos

def wordl():

    return wordlist

## Save all the words of interest
dataframe=pd.DataFrame(columns=['r1','r2'])
dataframe['r1']=wordlist
dataframe['r2']=wordpos

dataframe1=pd.DataFrame(wordlist)
dataframe1=dataframe1.drop_duplicates(keep="first")



dataframe.to_csv('wordlist1.csv',index=0,header=0)
dataframe1.to_csv('wordlist.csv',index=0,header=0)



## Return metadata
def subtitledetail():
    return starttime,endtime

