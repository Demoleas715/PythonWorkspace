'''
Created on Nov 30, 2015

@author: Evan
'''
class Student (object):
    def __init__(self, lastName, firstName, teacher="Respass"):
        self.lastName=lastName
        self.firstName=firstName
        self.teacher=teacher
        self.__grades=[]
        
    def addGrade(self, grade):
        self.__grades.append(grade)
        
    def addGrades(self, gradeStr):
        gradeList=gradeStr.split()
        for grade in gradeList:
            self.__grades.append(float(grade))
        
    def getAverage(self):
        return sum(self.__grades)/len(self.__grades)
    
    def __str__(self):
        return self.lastName + ", " + self.firstName + " %.2f" % (self.getAverage())
    