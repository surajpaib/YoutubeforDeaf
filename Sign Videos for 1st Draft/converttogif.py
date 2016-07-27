# Convert .mp4 files to .gif files

from moviepy.editor import *
import pandas as pd
import glob
import os
df=pd.read_csv('metadata.csv')
mat=df['Filename'].as_matrix()



for val in mat:
    clip1 = VideoFileClip(val)
    time=(clip1.duration/2)
    clip1=clip1.subclip((0),(time))
    k=str(val).split(".")
    t=str(k[0]).replace("'","")
    clip1.write_gif("GIFFiles2/"+str(t)+".gif", loop=0)











