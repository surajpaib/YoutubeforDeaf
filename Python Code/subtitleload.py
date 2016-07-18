import pycaption
from pycaption import detect_format
from pycaption import SRTWriter
from pycaption import WebVTTReader
import io

def Subtitleload(inputfile):
    wttcaps=io.open(inputfile,"r",encoding='utf-8').read()
    converter = pycaption.CaptionConverter()
    converter.read(wttcaps, WebVTTReader())
    srtcaps = io.open('subtitle.srt', "w", encoding='utf-8')
    srtcaps.write(converter.write(SRTWriter()))




