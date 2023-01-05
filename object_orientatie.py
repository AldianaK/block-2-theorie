"""
Author: Aldiana Kucevic
Date: 29-12-2022
Function: Classes and object oriented programming (h10)
"""

# encapsulatie voorbeeld Fasta

class Fasta:


    def setHeader(self, header):
        self.__header = header

    def getHeader(self):
        return self.__header

def main():
    f = Fasta()
    f.setHeader("NR_114752.1_Chlorobiales") # geeft een betekenis
    print(f.getHeader()) # print wat je als header hebt

main()

class Student:

    def setStudent(self, student):
        self.student = student

    def getStudent(self):
        return self.student

def main():

    aldiana = Student()
    aldiana.setStudent("Aldiana")
    print(aldiana.getStudent())
    isa = Student()
    isa.setStudent("Isa")
    print(isa.getStudent())
    roos = Student()
    roos.setStudent("Roos")
    print(roos.getStudent())

main()






