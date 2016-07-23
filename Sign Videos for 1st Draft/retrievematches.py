import re
import glob
import os
from downloadvideos import woi
from subprocess import call
import re



## The function to return the list of words is called
searchwords = woi()

## All files under the directory with .mp4, .mkv and .wmv extensions are loaded into list "file"
file=glob.glob("*.mp4")
file.extend(glob.glob("*.mkv"))
file.extend(glob.glob("*.wmv"))
filename=[]

for f in file:

    for k in searchwords:
        ## Regular expression to match files that correspond to words in the word list.
        regex=r"^('"+str(k)+"(s|ing)*'\.m.*)$"
        comp=re.compile(regex,flags=re.IGNORECASE)
        if comp.search(f):
            filename.append(f)

## Function returns all the matched files

def filematches():
    return filename





