def name(fname):
    print("my first name is:"+ fname)
name("abhinav karki")

def child(*kids):
    print("the oldest child in the family is:"+ kids[1])
child("abhi","abhinav","aabhi")
#keyword arguments
def cars(car1,car2,car3):
    print("the most expensive car brand is:"+ car2)
cars(car1="bmw",car3="lamborgini",car2="rolls royce")

#aribitary keyword arguments:
def car(**carname):
    print("the no of sale  of car company is:"+ carname["selling"])
car(name="toyata",selling="50")
car(name="ford",selling="22")
#default parameters:
def my_function(country = "Nepal"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#recursion example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(8)