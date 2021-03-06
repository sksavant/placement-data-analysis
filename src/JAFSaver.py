#!/usr/bin/python

from JAF import JAF
from placementsWeb import PlacementsWeb
from JAFReader import JAFReader
import os

error_string = 'Error!!!! please try again'

def writeJAFtoFile(cn, jn, html):
    try:
        f = open("../data/"+cn+str(jn)+".html",'r')
        if f.read()==html:
            f.close()
            return
    except IOError:
        pass
    if not os.path.exists("../data"):
        os.mkdir("../data/")
    f = open("../data/"+cn+str(jn)+".html",'w')
    f.write(html)
    f.close()

class JAFSaver:
    def __init__(self):
        self.p = PlacementsWeb()
        self.p.login()
        self.linklist = self.p.getJAFLinks()

    def getAllJAFs(self):
        for l in self.linklist:
            cn,jn,html = self.p.getLinkJAFPage(l)
            j = JAF(cn,jn)
            jr = JAFReader(html,j)
            jr.parseInfo()
            print j.getJAFString()
            break

    def saveAllHTML(self):
        for l in self.linklist:
            cn,jn,html = self.p.getLinkJAFPage(l)
            writeJAFtoFile(cn,jn,html)
            print cn,jn

    def printJAFHTML(self,compname, jafno):
        try:
            cn,jn,html = self.p.getCompJAFPage(compname, jafno)
            writeJAFtoFile(cn,jn,html)
            return True
        except Exception as e:
            print e
            return False

    def printAllJAFs(self, compname):
        i=1
        while self.printJAFHTML(compname,i):
            print "Getting JAF number",i
            i=i+1

    def printMissingJAFs(self):
        f = open('../data/missing-comp.txt','r')
        while True:
            x = f.readline().split()
            if x==[]:
                break
            cn = x[0]
            jn = int(x[1])
            #self.printJAFHTML(cn,jn)
            # Try all missing jaf numbers
            for i in range(1,6):
                self.printJAFHTML(cn,i)

if __name__=='__main__':
    #getAllJAFs()
    s = JAFSaver()
    s.saveAllHTML()
    #s.printJAFHTML('walmart',5)
    #s.printMissingJAFs()
