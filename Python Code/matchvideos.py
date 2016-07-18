import glob
import fnmatch
from readsrtfileandnlp import wordl

wordlist=wordl()

for word in wordlist:
    for name in glob.glob('C:\Users\Suraj\Desktop\Signs Dataset\*\*'):
        if fnmatch.fnmatch(name,word):
            print name
