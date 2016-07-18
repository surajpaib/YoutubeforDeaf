import sys
import youtube_dl
import submarine
import nltk
import pysrt
from subprocess import check_output
import subprocess
from IPython.utils.capture import capture_output as c
from subtitleload import Subtitleload



# Call subprocess to run command on cmd to get subtitle filename
command="youtube-dl -o %(title)s%(id)s --get-title --skip-download https://www.youtube.com/watch?v=qdfmIUO__y8"
output=[]
output=check_output(command.split(),shell=True)
output=output.strip()
output=output+".en.vtt"


# Call subprocess to download .vtt subtitle file without downloading video
command2="youtube-dl -o %(title)s --skip-download --write-auto-sub --sub-lang en https://www.youtube.com/watch?v=qdfmIUO__y8"
subprocess.call(command2.split(),shell=True)


Subtitleload(output)














