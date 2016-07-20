import nltk
import pysrt
from nltk import word_tokenize
from catergorize import cattags
import pandas as pd

sub=pysrt.open('subtitle.srt')
starttime=[]
endtime=[]
text=[]
for i in range(len(sub)):
    case=sub[i]
    text.append(case.text)
    starttime.append(case.start)
    endtime.append(case.end)

verbset,verbpos,nounset,nounpos,pronset,pronpos,adjecset,adjpos,advset,advpos,adpset,adppos,conjset,conjpos,detset,detpos,numset,numpos,prtset,prtpos,xset,xpos=cattags(text)
wordlist=nounset+verbset+adjecset


def wordl():

    return wordlist


dataframe=pd.DataFrame(wordlist)

dataframe=dataframe.drop_duplicates(keep='first')

dataframe.to_csv('wordlist1.csv',index=0,header=0)





