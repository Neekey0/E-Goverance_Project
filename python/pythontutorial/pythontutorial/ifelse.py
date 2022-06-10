a=17
if a>15:
    print("given number is greater than 15")
    if a>20:
        print("Given number is greater than 20")
    else:
        print("and the number is less than 20")

i=0
while i<8:
    print(i)
    if i==3:
        break
    i+=1

b=0
while b<8:
    b+=1
    if b==3:
        continue#stop the current iterarion and beigns form new one or next one
    print(b)
else:#exectutes when while condition is no longer true
    print("the iteration is finished...")