# Fibonacci
n=int(input("Enter the number for sequence: "))
a=0
b=1
for i in range(n):
    print(a)
    print(b)
    c=a+b
    a=b
    b=c
    print(c)
    
# Factorial of an number:
    
num=int(input("enter the num:  "))
fact=1
if num <0:
    print("enter positive number")
elif num==0:
    print("1")
else:
    for i in range(1,num+1):
        fact=fact*i
        print(fact)
       # print(f" fact of {num} is: {fact}")
       
# while loop


i=0
while i < 100:
    i += 1
    if i==51:
        continue
    
    print(i)