#program to print fibonacci series

n=int(input())
f0=0;f1=1
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for i in range(2,n+1):
        fi=f0+f1
        f0=f1
        f1=fi
        print(fi,end=" ")


    
