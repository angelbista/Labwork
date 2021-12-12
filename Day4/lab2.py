#Write a Python program to sum three given integers. However,if two or more values are equal sum will be zero.
a=int(input("enter the first integer"))
b=int(input("enter the second integer"))
c=int(input("enter the third integer"))
sum=a+b+c
if a==b or b==c or a==c:
    print("The sum is zero")
else:
    print(f"The sum is{sum}")