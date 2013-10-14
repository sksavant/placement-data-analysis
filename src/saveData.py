#!/usr/bin/python

from JAF import JAF
from placementsWeb import PlacementsWeb
from JAFReader import JAFReader

def getAllJAFs():
    p = PlacementsWeb()
    p.login()
    for l in p.getJAFLinks():
        cn,jn,html = p.getJAFPage(l)
        j = JAF(cn,jn)
        jr = JAFReader(html,j)
        jr.parseInfo()
        print j.getJAFString()
        break

def saveAllHTML():
    p = PlacementsWeb()
    p.login()
    for l in p.getJAFLinks():
        cn,jn,html = p.getJAFPage(l)
        print cn,jn
        f = open("../data/"+cn+str(jn)+".html",'w')
        f.write(html)
        f.close()

if __name__=='__main__':
    #getAllJAFs()
    saveAllHTML()
