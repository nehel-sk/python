y=int(input("Enter the year:"))
if(y%400==0 and y%100==0):
    print(y,"is a Leap year")
elif(y%4==0 and y%100!=0):
    print(y,"is a Leap Year")
else:
    print(y,"is not a Leap Year")
