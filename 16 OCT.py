# GRADE PROGRAM

X=int(input("Enter the marks "))


if X>=90 and X<= 100:
    print('You have Grade "A"')
elif X>=80 and X<=89:
    print('You have Grade "B"')
elif X>=70 and  X<=79:
    print('You have Grade "C"')
elif X>=60 and X<=69:
    print('You have Grade "D"')
elif X>=50 and X<=59:
    print('You have Grade "E"')
else:
    print("You are failed...!")
    
# LEAP YEAR PROGRAM
year=int(input("enter the year  "))
if year % 4==0 and year % 100 != 0:
    print(f"{year} is leap year")

elif year % 400==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
    
#TRIANGLE CLASSIFIER

print("Enter the slides..!")
s1=int(input())
s2=int(input())
s3=int(input())
if s1==s2==s3:
    print(" equilateral triangle")
elif s1==s2 and s1!=s3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    
