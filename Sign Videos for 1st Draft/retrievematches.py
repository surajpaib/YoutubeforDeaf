import re
import glob
import os
from downloadvideos import woi




searchwords = woi()

for row in searchwords:
    for filename in glob.glob("*.mp4"):
        k = filename.replace("'", "")
        print k
        print str('[' + str(row[0].upper()) + str(row[0].lower()) + ']' + str(row[1:])+"[.]mp4")
        c=re.search(str('['+str(row[0].upper())+str(row[0].lower())+']'+str(row[1:])+"[.]mp4"),k)

        print c


