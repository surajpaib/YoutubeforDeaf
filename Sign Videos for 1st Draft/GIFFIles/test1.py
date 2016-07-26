import moviepy
from moviepy.editor import *
import glob


clip=VideoFileClip('F:\DISQ Files\YoutubeforDeaf\Python Code\What A Wonderful World With David Attenborough -- BBC One [FULL HD].mp4')

clip.write_videofile('Test/MainVideo.mp4', fps=10)
















