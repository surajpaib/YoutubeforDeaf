from moviepy import *
from moviepy import editor
from moviepy.editor import *
import pandas as pd

df=pd.read_csv('../Sign Videos for 1st Draft/metadatafinal.csv')
startt=[]
endt=[]
stime=df['StartTime'].as_matrix()
etime=df['EndTime'].as_matrix()
word=df['WordOrder'].as_matrix()
filename=df['Filename'].as_matrix()
for s in stime:
    k=s.split(":")
    l=int(k[0])*60*60
    i=int(k[1])*60
    t=k[2].split(",")
    j=float(t[1])/1000
    sseconds=float(l+i+j+int(t[0]))
    startt.append(sseconds)

for st in etime:
    k = st.split(":")
    l = int(k[0]) * 60 * 60
    i = int(k[1]) * 60
    t = k[2].split(",")
    j = float(t[1]) / 1000
    eseconds = float(l + i + j + int(t[0]))
    endt.append(eseconds)
clip1 = VideoFileClip('..\Python Code\What A Wonderful World With David Attenborough -- BBC One [FULL HD].mp4')
for i in range(2):
    print startt[i],endt[i],word[i],filename[i]

    clip2=(VideoFileClip('..\Sign Videos for 1st Draft\GIFFiles\\'+filename[i],audio=False))
    clip2 = clip2.set_duration(2)
    clip2 = clip2.set_position(('right', 'bottom'))
    clip2 = clip2.fx(vfx.resize, height=220, width=220)
    if (word[i]) == 0:
        clip2 = clip2.set_start(startt[i]+((endt[i]-startt[i])/5))
    if (word[i]) == 1:
        clip2 = clip2.set_start(startt[i]+(1.25*(endt[i]-startt[i])/5))
    if (word[i]) == 2:
        clip2 = clip2.set_start(startt[i]+(1.5*(endt[i]-startt[i])/5))
    if (word[i]) == 3:
        clip2 = clip2.set_start(startt[i]+(2*(endt[i]-startt[i])/5))
    if (word[i]) == 4:
        clip2 = clip2.set_start(startt[i]+(2.25*(endt[i]-startt[i])/5))
    if (word[i]) == 5:
        clip2 = clip2.set_start(startt[i]+(2.5*(endt[i]-startt[i])/5))




    clip=CompositeVideoClip([clip1,clip2])
    clip1=clip






clip1.write_videofile('movie.mp4',fps=15)











