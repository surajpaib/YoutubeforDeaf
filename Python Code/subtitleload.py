import pycaption
from pycaption import detect_format
from pycaption import SRTWriter
from pycaption import WebVTTReader
import io


# Convert from WebVTT to SRT
def Subtitleload(inputfile):
    wttcaps=io.open(inputfile,"r",encoding='utf-8').read()
    converter = pycaption.CaptionConverter()
    #Captionset object as intermediary

    converter.read(wttcaps, WebVTTReader())
    srtcaps = io.open('subtitle.srt', "w", encoding='utf-8')
    #Write converter object into srtcaps file
    srtcaps.write(converter.write(SRTWriter()))




