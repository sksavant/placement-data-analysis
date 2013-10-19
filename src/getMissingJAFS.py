#!/usr/bin/python
from JAFSaver import JAFSaver

s = JAFSaver()
print "Company name :",
cn = raw_input()
s.printAllJAFs(cn)
