print("hello world")
if 5 > 2:
 print("Five is greater than two!")
#this is a comment
print("hello world")
x=55
print(type(x)) #gives data types 

#unpacking examples 
fruits=["apple","banana","orange"]
x,y,z = fruits
print(x,y,z)
fruits[1]="blueberries"
fruits.insert(1,"strawberries")
print(fruits)
#print(y)

#random number generatio using random module
import random
print(random.randrange(1,1000))
a=str(69.69)
print(a)

#multiline string
a="""this is the
example of multiline string,
i like it."""
print(a)

#string as array (single character is of length 1)
a=("hello world , this is the new world")
print(a[5])#counters white space also 
print(a[:4])#slicing an string(4 is not included)
print(a[0:])

#check string
txt="this is the example of check string"
if "check" in txt:
    print('check is present in the string')

#string format (combines strings and numbers )
roll=23
info="my name is abhinav karki and my roll.no is {}"
print(info.format(roll))

#escape character
txt="this is the example\'s of \"escpae\" charcater"
print(txt)
#A backslash followed by an 'x' and a hex number represents a hex value:
txt1 = "\x48\x65\x6c\x6c\x6f"
print(txt1)

#string method:
a="ABHI karki"
print(a.capitalize())   
print(a.casefold())
print(a.center(60))

#boolean false value
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

x=500.55
print(isinstance(x,int))

#list examples
#extending a list 
a=["apple","banana","cherry"]
b=["pizza","burger","fries"]
c=("bmw","ford","thar")
a.extend(b)
print(b)
b.extend(c)
print(b)
