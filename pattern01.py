'''program to print the pattern
          A
         A B
        A B C
'''


n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(ord('A')+k-1),end=" ")
    print()
