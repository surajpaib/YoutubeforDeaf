import nltk
import pysrt
from nltk import word_tokenize
from catergorize import cattags


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


print nounset+verbset+adjecset
