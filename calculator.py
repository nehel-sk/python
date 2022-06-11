print("\t\tCALCULATOR")
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
print("\n1.Addition\n2.Substration\n3.Multiplication\n4.Division\n")
ch=int(input("Enter your choice:"))
if(ch==1):
    sum=n1+n2
    print("Addition:",sum)
elif(ch==2):
    diff=n1-n2
    print("Substraction:",diff)
elif(ch==3):
    mul=n1*n2 
    print("Multiplication:",mul)
elif(ch==4):
    if(n2==0):
        print("Division by zero is not difined")
    else:
        div=n1/n2
        print("Division:",div)
else:
    print("Invalid choice!!")


