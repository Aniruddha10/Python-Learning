# -*- coding: utf-8 -*-
class Alien:
    __name = ""
    __planet = ""
    displayname = ""
    totalaliens = 0
    def __init__(self, name, planet, displayname):
        self.__name = name
        self.__planet = planet
        self.displayname = displayname
        Alien.totalaliens += 1    
    def greeting(self):
        print ('Hello I am {} from planet {}'.format(self.__name, self.__planet))
        #print('How are you {}'.format(self.alien.displayname))
    #def greet(self, Alien):
    
    def __str__(self):
        return self.__name
    
    def __del__(self):
        print("deleting "+ str())
    
    
def main():
    alien1 = Alien("dwarf1", "pluto", "dwarf1")
    alien1.greeting()
    print(alien1.displayname)
    
    alien2 = Alien("jup1", "jupiter", "jup1")
    alien2.greeting()
    print(alien2.displayname)
    
main()
