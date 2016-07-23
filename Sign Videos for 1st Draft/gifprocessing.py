import moviepy
import sys
import csv
import pysrt
sys.path.append('..\Python Code')
import readsrtfileandnlp as rsf
import retrievematches as rm
import pandas as pd

filename=rm.filematches()
start,end=rsf.subtitledetail()
ifile=open('..\Python Code\wordlist1.csv',"rb")
reader=csv.reader(ifile)
filelist=[]
stime=[]
etime=[]
wordno=[]
flist=[]

for row in reader:
    for f in filename:
        if (f.replace("'","")==str(row[0])+".mp4"):
            k=row[1].split(".")
            t = int(k[0])
            if len(k)==1:
                k.append(0)

            t1 = int(k[1])

            stime.append(start[t])
            etime.append(end[t])
            wordno.append(t1)
            flist.append(f)

        df = pd.DataFrame(columns=['StartTime', 'EndTime', 'WordOrder', 'Filename'])
        df['StartTime'] = stime
        df['EndTime'] = etime
        df['WordOrder'] = wordno
        df['Filename'] = flist

        df.to_csv('metadata.csv', index=0)











