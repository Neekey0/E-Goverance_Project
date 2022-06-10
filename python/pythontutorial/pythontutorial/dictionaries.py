#keys update in dicationaries
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
y=car.values()
z=car.items()
print(x) #before the change
print(y)
print(z)
car["color"] = "white"
print(x) #after the change
print(y)
print(z)
if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")

cars = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
cars["color"]="red" #adding items in dictionaries
cars.update({"year":2021})#keys:value pair mah hunu parcha(also use for adding items)
print(cars)
#print all the value one by one
for i in car:
    print(car[i])
#loops
vehicle={
"brand": "BMW",
"model": "sports",
"year": 1900
}
for a in vehicle.values():
    print(a)
for b in vehicle.keys():
    print(b)
for x,y in vehicle.items():
    print(x,"=",y)
#copying
vehicle1= vehicle.copy()
print("this is the example of copy method")
print(vehicle1)
vehicle2=dict(vehicle1)
print("this is the example of copying using dict() function")
print(vehicle2)

#nested dictionary
print("this is the exapmle of nested dictionary:")
myfamily = {
  "child1" : {
    "name" : "joe",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobi",
    "year" : 2007
  },
  "child3" : {
    "name" : "moni",
    "year" : 2011
  }
}
print(myfamily)
