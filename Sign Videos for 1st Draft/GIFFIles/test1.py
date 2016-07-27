import moviepy
from moviepy.editor import *
import glob


for f in glob.glob("*.gif"):
    y=f.split(".")
    k=y[0]+".mp4"
    clip=VideoFileClip(f)
    img = clip.to_ImageClip(0.1)
    img1 = clip.to_ImageClip(0.5)
    img2 = clip.to_ImageClip(0.75)
    img3 = clip.to_ImageClip(1)
    img4 = clip.to_ImageClip(1.25)
    img5 = clip.to_ImageClip(1.5)
    img6 = clip.to_ImageClip(1.75)


    clip = concatenate([img, img1, img2, img3, img4, img5, img6, img7])
    clip.write_videofile('Test/'+k, fps=10)
















