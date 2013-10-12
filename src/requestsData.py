#!/usr/bin/python
import requests

placement_login_page = 'http://placements.iitb.ac.in/placements/login.jsp'
placement_home = 'http://placements.iitb.ac.in/placements/studenthome.jsp'

NO_PROXY={
        "http" : "",
        "https" : "",
        }

auth = {
        "ldaplogin" : "",
        "ldappasswd" : "",
        }

#response = requests.get(placement_login_page, stream=True, proxies=NO_PROXY)
#response.read.raw()
s = requests.Session()
r = s.get(placement_login_page, stream=True, proxies=NO_PROXY)
#print r.raw.read()
rlogged = s.post(placement_login_page, data=auth, stream=True, proxies=NO_PROXY)
#print rlogged.raw.read()
rhome = s.get(placement_home, stream=True, proxies=NO_PROXY)
print rhome.raw.read()
