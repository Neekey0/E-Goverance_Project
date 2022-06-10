class person:
    def  __init__(self,name,age):
        self.name=name 
        self.age=age 
    def myfunc(self):
        print("my name is:"+ self.name)
p1=person("abhinav",21)
print(p1.name)
p1.age=69 #modifying the object value
print(p1.age)
p1.myfunc()

print("Below is the example of self parameter")
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("abhi", 30)
p1.myfunc()
#objects
print("object declaring")
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

#super function
print("this is done by using super function")
class parent1:
    def func1(self):
        print("this is the function 1")

class child1(parent1): 
    def func2(self):
        super().func1()
        print("this is the function 2")
obj1=child1()
obj1.func1()
obj1.func2()
#method overwrithing
print("this is the exapmles of method overriding")
class parent2:
    def func1(self):
        print("this is the function 1")

class child2(parent2): 
    def func1(self):
        #super().func1()
        print("this is the function 2")

obj2=child2()
obj2.func1()