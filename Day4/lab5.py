#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

a=int(input("number of classes held"))
b=int(input("number of classes attended"))
c=(b/a)*100
if c>75:
    print("student is allowed to sit in exam")
else:
    print("student is not allowed to sit in exam")