#!/usr/bin/python
import getpass

class Authentication:
    def __init__(self):
        self.username=""
        self.password=""
        self.gotauth=False
        self.get_from_file()
        if not self.gotauth:
            self.get_from_input()
        if self.gotauth:
            pass
        else:
            print "Looped once but not got any auth"
            self.__init__()

    def get_from_file(self):
        try:
            if not self.gotauth:
                f=open(".auth","r")
                self.username,self.password=f.read().split()
                self.gotauth=True
                f.close()
        except:
            self.gotauth=False

    def get_from_input(self):
        self.username=raw_input("Username :")
        self.password=getpass.getpass() #To mask password
        self.gotauth=True
        f=open(".auth","w")
        f.write(self.username+" "+self.password)
        f.close()

if __name__ == "__main__":
    auth=Authentication()
