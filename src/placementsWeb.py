#!/usr/bin/python
import mechanize
import cookielib
import re
import json
from authenticate import Authentication
from mechanize import Link

placement_login_page = "http://placements.iitb.ac.in/placements/login.jsp"
placement_home = 'http://placements.iitb.ac.in/placements/studenthome.jsp'
placement_jafs_page = 'http://placements.iitb.ac.in/placements/studjaf4studnew.jsp'
jaf_base_url = 'http://placements.iitb.ac.in/placements/studjaf4studnew.jsp'
compnameregex = re.compile('(?<=\?complogin\=)\S+(?=&jafsrno)')
jafnoregex = re.compile('(?<=\&jafsrno\=)[0-9]+')
jafpageurlregex = re.compile('http\:\/\/placements\.iitb\.ac\.in\/placements\/studjafview\.jsp\?complogin\=\S+\&jafsrno\=[0-9]+')
signpageurlregex = re.compile('http\:\/\/placements\.iitb\.ac\.in\/placements\/studsign\.jsp\?complogin\=\S+\&jafsrno\=[0-9]+')

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

    def goToJAFsPage(self):
        try:
            assert self.br.geturl() == placement_jafs_page
        except AssertionError:
            print "Going to JAF List page first"
            self.br.find_link(text='View / Sign JAFs')
            req = self.br.click_link(text='View / Sign JAFs')
            self.br.open(req)
            #print br.response().read()
            assert self.br.geturl() == placement_jafs_page

    def getJAFLinks(self):
        self.goToJAFsPage()
        no_of_jafs = 0
        linklist = list(self.br.links(url_regex=re.compile('studjafview')))
        print "Got links to",len(linklist),"JAFs"
        return linklist
        #for l in linklist:
        #    no_of_jafs = no_of_jafs+1
        #    self.getJAFInfo(l)
        #print no_of_jafs

    def getCompJAFPage(self, compname, jafno):
        self.goToJAFsPage()
        _url='studjafview.jsp?complogin='+compname+'&jafsrno='+str(jafno)
        l = Link(base_url=jaf_base_url, url=_url, text=compname, tag='a', attrs=[('href',_url)])
        req = self.br.click_link(l)
        self.br.open(req)
        html = self.br.response().read()
        self.br.back()
        if 'Error!!!! please try again' in html:
            raise Exception('No JAF no. '+str(jafno)+' of '+compname)
        return compname,jafno,html

    def getLinkJAFPage(self,l):
        req = self.br.click_link(text=l.text)
        self.br.open(req)
        assert jafpageurlregex.match(self.br.geturl())
        #print 'Getting JAF Info for',l.text,":",l.url
        compname = compnameregex.findall(l.url)[0]
        jafno = jafnoregex.findall(l.url)[0]
        #print compname,jafno
        html = self.br.response().read()
        self.br.back()
        return compname,jafno,html

    def getAllSignLinks(self):
        self.goToJAFsPage()
        linklist = list(self.br.links(url_regex=re.compile('studsign')))
        return linklist

    def getAllUnSignLinks(self):
        self.goToJAFsPage()
        linklist = list(self.br.links(url_regex=re.compile('studunsign')))
        return linklist

    def signJAFLink(self, l):
        self.goToJAFsPage()
        print l
        compname = compnameregex.findall(l.url)[0]
        jafno = jafnoregex.findall(l.url)[0]
        _url='studsign.jsp?complogin='+compname+'&jafsrno='+str(jafno)
        l = Link(base_url=jaf_base_url, url=_url, text=compname, tag='a', attrs=[('href',_url)])
        req = self.br.click_link(l)
        self.br.open(req)
        print self.br.geturl()
        assert signpageurlregex.match(self.br.geturl())
        self.br.select_form(nr=0)

        #self.br.form.set_value(['1'],name='copyno')
        #self.br.submit()
        #self.br.back()

if __name__=='__main__':
    p = PlacementsWeb()
    p.login()
    #print p.getJAFLinks()
    #jafpagetest = 'http://placements.iitb.ac.in/placements/studjafview.jsp?complogin=tsmc&jafsrno=1'
    #print jafpageurlregex.findall(jafpagetest)
    x = p.getAllSignLinks()
    p.signJAFLink(x[0])

