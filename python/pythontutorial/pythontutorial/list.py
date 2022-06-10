#loop lists
a=["apple","banana","chery"]
for x in [a]:
     print(x)
#looping through indexed number
for x in range(len(a)):
    print(a[x]) 

#while loop
b=["a","b","c","d"]
i=0
while i<len(b):
    print(b[i])
    i=i+1

#list comprehension
s=["abhi","pheebs","cathy","joe","mon"]
newlist=[x for x in s if "a" in x]
print(newlist)

newlist1=[x.upper() for x in s if x!="abhi"]
print(newlist1)

#joining lists
l=["ab","cd","ef","gh"]
m=["ij","kl","mn","op","qr"]
for i in m:
    l.append(i)
print(l)
#extend()
t=["ab","cd","ef","gh"]
y=["ij","kl","mn","op","qr"]
y.extend(t)
print(y)

