from Student import Student

def readStudentList():
    studentList=[]
    
    ln=input("What is the last name of the first person\n")
    
    while(len(ln)>0):
        fn=input("What is their first name\n")
        grades=input("What are the grades -- input on one line")
        
        s=Student(ln, fn)
        s.addGrades(grades)
        studentList.append(s)
        
        ln=input("What is the last name of the next person\n")
    
    return studentList

def printStudentList(studentList):
    for s in studentList:
        print(s)
        
def main():
    myStudentList=readStudentList()
    myStudentList.sort(key=Student.getAverage, reverse=True)
    printStudentList(myStudentList)
    
main() 
