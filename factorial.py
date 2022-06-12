n=int(input("Enter the number whose factorial is to be found:"))
num=n
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of ",num,"is",fact)
