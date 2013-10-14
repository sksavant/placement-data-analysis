#!/usr/bin/python
import re
from JAF import JAF
from bs4 import BeautifulSoup

class JAFReader:
    def __init__(self,html,j):
        self.soup = BeautifulSoup(html)
        self.jaf = j

    def parseInfo(self):
        print "Getting info from html"
        #self.jaf.compname = "test" can change :D
        # @TODO

    def printPrettyHTML(self):
        print self.soup.prettify()

if __name__=='__main__':
    f = open("../data/tsmc.html")
    html = f.read()
    j = JAF("tsmc",1)
    jr = JAFReader(html,j)
    jr.parseInfo()
    jr.printPrettyHTML()
