file= open ('students.txt')
students = file.read() 
print (students)
students = students+"\nOlive Yew"+"\nAida Bugg"+"\nMaureen Biologist"+"\nTeri Dactyl"
file= open ('students.txt','w')
file.write(students)
file.close()

n=input("write the name of the student : ")
file=open('students.txt') 
if(n in file.readline() ):
    print("yes the name exist in the list")
else: 
     print("the name doesn't exist in the list ")



