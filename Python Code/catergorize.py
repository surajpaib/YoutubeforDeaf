import nltk
from nltk import word_tokenize


def cattags(text):
    nounset = []
    nounpos = []
    verbset = []
    verbpos = []
    adjecset = []
    adjpos = []
    pronset = []
    pronpos = []
    advset = []
    advpos = []
    prtset = []
    prtpos = []
    detset = []
    detpos = []
    numset = []
    numpos = []
    conjset = []
    conjpos = []
    adpset = []
    adppos = []
    xset = []
    xpos = []

    for i in range(len(text)):

        tokens = word_tokenize(text[i])
        nlptext = nltk.pos_tag(tokens, tagset='universal')
        for j in range(len(nlptext)):
            if (nlptext[j][1] == "NOUN"):
                nounset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                nounpos.append(pos)
            if (nlptext[j][1] == "VERB"):
                verbset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                verbpos.append(pos)
            if (nlptext[j][1] == "ADJ"):
                adjecset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                adjpos.append(pos)
            if (nlptext[j][1] == "PRON"):
                pronset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                pronpos.append(pos)
            if (nlptext[j][1] == "ADV"):
                advset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                advpos.append(pos)
            if (nlptext[j][1] == "PRT"):
                prtset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                prtpos.append(pos)
            if (nlptext[j][1] == "DET"):
                detset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                detpos.append(pos)
            if (nlptext[j][1] == "NUM"):
                numset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                numpos.append(pos)
            if (nlptext[j][1] == "CONJ"):
                conjset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                conjpos.append(pos)
            if (nlptext[j][1] == "ADP"):
                adpset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                adppos.append(pos)
            if (nlptext[j][1] == "X"):
                xset.append(nlptext[j][0])
                pos = int(str(i) + str(j))
                xpos.append(pos)

    return verbset, verbpos, nounset, nounpos, pronset, pronpos, adjecset, adjpos, advset, advpos, adpset, adppos, conjset, conjpos, detset, detpos, numset, numpos, prtset, prtpos, xset, xpos
