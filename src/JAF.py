#!/usr/bin/python

class JAF:
    def __init__(self, compname, jafno, companytype="", jaftype="", category="", job_description="", bond=0, places="", salary=[] , additional_info=""):
        self.salary_index = ["B.Tech", "Integrated M.Sc.", "M.Tech", "M.Sc", "Dual Degree"]
        self.compname = compname # String 
        self.jafno = jafno
        self.companytype = companytype
        self.jaftype = jaftype
        self.category = category # String
        self.job_description = job_description #DocString?
        self.bond = bond #Number of months; 0 if no bond
        self.places = places.split('/')
        self.salary = []
        self.additional_info = additional_info

    def setCompanyType(self, companytype):
        self.companytype = companytype

    def setJAFType(self, jaftype):
        self.jaftype = jaftype

    def setCategory(self, category):
        self.category = category

    def setJobDescription(self, job_description):
        self.job_description = job_description

    def setBond(self, bond):
        self.bond = bond

    def setPlaces(self, places):
        self.places = places.split('/')

    def setSalary(self, salary):
        self.salary = salary

    def setAdditionalInfo(self, additional_info):
        self.additional_info = additional_info

    def getJAFString(self):
        s = self.compname+"\n"
        s += "JAF No. \t\t: "+str(self.jafno)+"\n"
        s += "Company Type \t\t: "+self.companytype+"\n"
        s += "JAF Type \t\t: "+self.jaftype+"\n"
        s += "Category \t\t: "+self.category+"\n"
        s += "Job Descr \t\t: "+self.job_description+"\n"
        s += "Bond      \t\t: "+str(self.bond)+" months\n"
        s += "Place    \t\t: "+str(self.places)+"\n"
        return s

if __name__=='__main__':
    j = JAF("deutschebank", 2)
    j.setCompanyType("A1")
    j.setJAFType("C1")
    j.setCategory("Analytics")
    j.setBond(0)
    j.setPlaces("Mumbai")
    print j.getJAFString()
