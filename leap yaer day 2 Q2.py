
n=int(input("enter the year"))
a=n%400
b=n%100
c=n%4
if(a==0 and b==0 and c!=0):
    print("leap year")
elif(n<=0):
    print("invalid input")
else:
    print("not a leap year")
    print("leap year",n-3)
