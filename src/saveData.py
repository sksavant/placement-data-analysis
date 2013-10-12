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
        self.auth = Authentication()
        assert (self.auth.username == "sk.savant")

        self.br = mechanize.Browser()
        self.cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cj)

        # Options
        self.br.set_handle_equiv(True)
        #br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)

        # Handling refresh
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Debug messages
        #br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)

        # User agent
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        self.br.set_proxies({})

    def login(self):
        print placement_login_page
        r = self.br.open(placement_login_page)
        html = r.read()

        n_forms = 0

        for f in self.br.forms():
            n_forms = n_forms+1

        assert (n_forms == 1)

        self.br.select_form(nr=0)

        self.br.form['ldaplogin'] = self.auth.username
        self.br.form['ldappasswd'] = self.auth.password
        self.br.submit()

        assert self.br.geturl() == placement_home

    def getJAFs(self):

        self.br.find_link(text='View / Sign JAFs')
        req = self.br.click_link(text='View / Sign JAFs')
        self.br.open(req)
        #print br.response().read()
        assert self.br.geturl() == placement_jafs_page
        no_of_jafs = 0
        for l in self.br.links(url_regex=re.compile('studjafview')):
            no_of_jafs = no_of_jafs+1
            self.getJAFInfo(l)

        print no_of_jafs

    def getJAFInfo(self,l):
        print 'Getting JAF Info for',l.text,":",l.url

if __name__=='__main__':
    p = PlacementsWeb()
    p.login()
    p.getJAFs()
