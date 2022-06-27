'''program to print pattern
    A
   B C
  D   E
 F     G
HIJKLMNOP
'''


n=int(input())
inc=0
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        if(k==1 or k==2*i-1 or i==n):
            print(chr(65+inc),end="")
            inc=(inc+1)%26
        else:
            print(" ",end="")
    print()
