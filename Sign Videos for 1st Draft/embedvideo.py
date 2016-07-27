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
wordmax=max(word)
print wordmax
filen=df['Filename'].drop_duplicates(keep={'first'}).as_matrix()
filename=[]

for f in filen:
    j='F:\DISQ Files\YoutubeforDeaf\Sign Videos for 1st Draft\GIFFIles2\\'+f

    filename.append(j)






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
clip1 = VideoFileClip('F:\DISQ Files\YoutubeforDeaf\Python Code\Solar System Lesson for Kids _ Turtlediary.mp4')
w,h=clip1.size
for i in range(len(filename)):
    print startt[i],endt[i],word[i],filename[i]

    clip2=(VideoFileClip(filename[i],audio=False))
    clip2 = clip2.set_duration(2)
    clip2 = clip2.set_position(('right', 'bottom'))
    clip2 = clip2.fx(vfx.resize, height=(h/5), width=(w/5))
    clip2 = clip2.set_opacity(0.7)
    for q in range(wordmax):
        if (word[i]) == q:
            clip2 = clip2.set_start(startt[i]+(q*0.5*(endt[i]-startt[i])/5))




    clip=CompositeVideoClip([clip1,clip2])
    clip1=clip






clip1.write_videofile('movie2.mp4',fps=15)










