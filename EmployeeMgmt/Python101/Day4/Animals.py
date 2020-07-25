# -*- coding: utf-8 -*-
class Animal:
    _dogcount=0
    
    def printmyname(self):
        print("It is me ")

class Dog(Animal):
    __name = ""
    def __init__(self,aname):
        self.__name = aname
        Dog._dogcount +=1
    def speak(self, sound):
        print('{} barking {}'.format(self.__name, sound))
    def jump(self):
        print('{} Jumped'.format(self.__name))    
    def __str__(self):
        return self.__name
    def shoucount(self):
        print("TOtal dogs {}".format(Dog._dogcount))
    def __del__(self):
        print("deleted "+self.__name)

def main():
    animal = Dog("Tommy")
    animal.speak("www")   
    animal.printmyname()
    animal.jump()     
        
    animal1 = Dog("Jimmy")
    animal1.speak("www 111")   
    animal1.printmyname()
    animal1.jump()     
    
    animal.shoucount()

main()