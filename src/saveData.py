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

def writeJAFtoFile(cn, jn, html):
    f = open("../data/"+cn+str(jn)+".html",'w')
    f.write(html)
    f.close()

def saveAllHTML():
    p = PlacementsWeb()
    p.login()
    for l in p.getJAFLinks():
        cn,jn,html = p.getJAFPage(l)
        writeJAFtoFile(cn,jn,html)
        print cn,jn

def printJAFHTML(compname, jafno):
    p = PlacementsWeb()
    p.login()
    cn,jn,html = p.getCompJAFPage(compname, jafno)
    writeJAFtoFile(cn,jn,html)

if __name__=='__main__':
    #getAllJAFs()
    #saveAllHTML()
    printJAFHTML("walmart",1)
