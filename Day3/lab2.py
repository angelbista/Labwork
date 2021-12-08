#WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail
a = int(input("enter marks for computer:"))
b = int(input("enter marks for english:"))
c = int(input("enter marks for economics:"))
d = int(input("enter marks for nepali:"))
totalmarks = a+b+c+d
print("Total score is", totalmarks)
percentage = (totalmarks / 400) *100
print("total percent is ", percentage, "%")
if percentage > 70:
    print("he got distinction")
elif percentage > 60:
    print("he got first division")
elif percentage > 40:
    print("he passed the exam")
elif percentage < 40:
    print("he failed")
