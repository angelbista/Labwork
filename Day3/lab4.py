
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if a<b and a<c:
    print(a,"the number is smallest")
elif b<a and b<c:
    print(b,"the number is smallest")
else:
    print(c,"the number is smallest")