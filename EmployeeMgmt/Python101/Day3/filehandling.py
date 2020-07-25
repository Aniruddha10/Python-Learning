
# -*- coding: utf-8 -*-

def readFile(filename):
    objMyFile = open(filename, 'r')
    strContent = objMyFile.read()
    lines = objMyFile.readlines()
    objMyFile.close()
    print(lines)
    print(strContent)
    
#readFile("C:\Self\PythonLearning\EmployeeMgmt\ProfileMgmt\SampleText.txt")
    
def writeFile(fileName):
    myFile = open(fileName, 'w')
    myFile.write("Dog, Cat\n")
    myFile.write("Tiger, Lion\n")
    myFile.write("Parrot, Pigion\n")
    myFile.close()
    
def appendFile(fileName):
    myFile = open(fileName, 'a')
    myFile.write("Hilsa, Salmon\n")
    myFile.write("snake, chamaleon\n")
    myFile.close()

def insertFile(fileName):
    objMyFile = open(fileName, 'r')
    lines = objMyFile.readlines()
    objMyFile.close()
    
    writeFile = open(fileName, 'w')
    lines.insert(1, "Fluffers, Samoyed\n")
    writeFile.writelines(lines)
    writeFile.close()
    
    
    
insertFile("Animals.txt")