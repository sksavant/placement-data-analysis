#!/usr/bin/python

from JAF import JAF
from placementsWeb import PlacementsWeb
from JAFReader import JAFReader

def writeJAFtoFile(cn, jn, html):
    f = open("../data/"+cn+str(jn)+".html",'w')
    f.write(html)
    f.close()

class JAFSaver:
    def __init__(self):
        self.p = PlacementsWeb()
        self.p.login()
        self.linklist = self.p.getJAFLinks()

    def getAllJAFs(self):
        for l in linklist:
            cn,jn,html = self.p.getJAFPage(l)
            j = JAF(cn,jn)
            jr = JAFReader(html,j)
            jr.parseInfo()
            print j.getJAFString()
            break

    def saveAllHTML(self):
        for l in linklist:
            cn,jn,html = p.getJAFPage(l)
            writeJAFtoFile(cn,jn,html)
            print cn,jn

    def printJAFHTML(self,compname, jafno):
        cn,jn,html = self.p.getCompJAFPage(compname, jafno)
        writeJAFtoFile(cn,jn,html)

    def printMissingJAFs(self):
        f = open('../data/missing-comp.txt','r')
        while True:
            x = f.readline().split()
            if x==[]:
                break
            cn = x[0]
            jn = int(x[1])
            #print cn,jn
            self.printJAFHTML(cn,jn)

if __name__=='__main__':
    #getAllJAFs()
    #saveAllHTML()
    s = JAFSaver()
    s.printMissingJAFs()
