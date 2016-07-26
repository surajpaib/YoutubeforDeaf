import moviepy
from moviepy.editor import *


clip=VideoFileClip('..\Python Code\What A Wonderful World With David Attenborough -- BBC One [FULL HD].mp4')
w,h=clip.size
clip1=VideoFileClip('..\Sign Videos for 1st Draft\GIFFiles\\tree.gif')
clip1=clip1.set_position(('right','bottom'))
clip1=clip1.set_duration(3)
clip1=clip1.set_start(1)
clip1=clip1.fx(vfx.resize,width=250,height=250)
video=CompositeVideoClip([clip,clip1])

video.write_videofile('test.mp4',fps=20)
