#!/usr/bin/python
import mechanize
import cookielib
import re
import json
from authenticate import Authentication

placement_login_page = "http://placements.iitb.ac.in/placements/login.jsp"
placement_home = 'http://placements.iitb.ac.in/placements/studenthome.jsp'
placement_jafs_page = 'http://placements.iitb.ac.in/placements/studjaf4studnew.jsp'

class PlacementsWeb:
    def __init__(self):
        auth = Authentication()
        assert (auth.username == "sk.savant")

        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)

        # Options
        br.set_handle_equiv(True)
        #br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)

        # Handling refresh
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Debug messages
        #br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)

        # User agent
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        br.set_proxies({})

    def login(self):
        print placement_login_page
        r = br.open(placement_login_page)
        html = r.read()

        n_forms = 0

        for f in br.forms():
            n_forms = n_forms+1

        assert (n_forms == 1)

        br.select_form(nr=0)

        br.form['ldaplogin'] = auth.username
        br.form['ldappasswd'] = auth.password
        br.submit()

        assert br.geturl() == placement_home

    def getJAFs(self):

        br.find_link(text='View / Sign JAFs')
        req = br.click_link(text='View / Sign JAFs')
        br.open(req)
        #print br.response().read()
        assert br.geturl() == placement_jafs_page
        no_of_jafs = 0
        for l in br.links(url_regex=re.compile('studjafview')):
            no_of_jafs = no_of_jafs+1
            getJAFInfo(l)

        print no_of_jafs

    def getJAFInfo(self,l):
        print l

if __name__=='__main__':
    p = PlacementsWeb()
    p.login()
    p.getJAFs()
