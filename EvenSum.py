#Program to find the sum of even numbers in a given sequence.

l=int(input("Enter the limit of the sequence:"))
i=1
sum=0
while(i<=l):
    if(i%2==0):
        sum=sum+i
    i=i+1
print("Sum of even numbers is",sum)