#Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR".
a=int(input("Enter the age"))
b=str(input("Enter the gender"))
if b=="female":
    print("she will work on urban areas")
elif b=="male" and a in range(20,40):
    print("He may work anywhere.")
elif b=="male" and a in range(40,60):
    print("He will work in urban area only.")
else:
    print("ERROR")