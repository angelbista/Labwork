#Given a n-digit number. Find the sum of its digits
a=int(input("enter a number"))
first_digit=a//10
second_digit=a%10
total=first_digit+second_digit
print("the sum of digit of the number entered is",total)