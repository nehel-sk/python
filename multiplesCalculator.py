#Program to find multiples of a number.

k=1
while(k<=70):
    print("#",end="")
    k=k+1
print("\n")
print("\t\tWELCOME TO MULTIPLER CALCULATOR")
s=int(input("enter the limit for the sequence:"))
i=int(input("enter the starting point:"))
n=int(input("enter the number who's multiples are to be printed:"))
print("the numbers are:")
while(i<=s):
    if(i%n==0):
        print(i)
    i=i+1
print("\t\tThank You For Using This Program")
k=1
while(k<=70):
    print("#",end="")
    k=k+1
