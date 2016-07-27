# Prepare Metadata with start time, end time and word order
import moviepy
import sys
import csv
sys.path.append('..\Python Code')
import readsrtfileandnlp as rsf
import retrievematches as rm
import pandas as pd

# Load functions from file to get timing and word information
filename=rm.filematches()
start,end=rsf.subtitledetail()
ifile=open('..\Python Code\wordlist1.csv',"rb")
reader=csv.reader(ifile)
filelist=[]
stime=[]
etime=[]
wordno=[]
flist=[]


# Extract information and store to metadata file
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











