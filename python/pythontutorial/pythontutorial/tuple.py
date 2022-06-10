#updating tuples
import abc


a=("abhi","abhii","abhinav","avi")
b=list(a)
b.append("karki")
c=tuple(b)
print(c)

#unpacking the tuples
a=("abhi","abhii","abhinav","avi","aaa","bbb")
(x,y,*z)=a 
print(x)
print(y)
print(z)

#sets method()
a={1,2,3,4,5,6,9}
b={7,8,9,10}
#c=a.difference(b)#only contains the item that exists in set a only
a.difference_update(b)
print(a)
#print(c)