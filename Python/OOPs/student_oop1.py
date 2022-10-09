class Student :
    def __init__(self,name,age): #constructor definition
        self.sname = name 
        self.sage = age
        #sname and sage are the actual attribute as they are bundled with the object 
        print("My name is {} and my age is {} ".format(self.sname,self.sage))
        #self will refer to the current object 
##to create objects of the class 

student1 = Student("Riya",18)
student2 = Student("Freak",20)
#object_name = class_name()
print(student1.sname)#fetching the attribute of an object 
