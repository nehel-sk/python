'''
To Write a Python program to check the validity of a password given by the user.The Password should satisfy the following criteria:
1. Contains at least one letter between a and z
2. Contains at least one number between 0 and 9
3. Contains at least one letter between A and Z
4. Contains at least one special character from $, #, @
5. Minimum length of password: 6

'''

d=0
u=0
l=0
sc=0
p=input("enter the password:")
if(len(p)>=6):
    for i in p:
        if(i.isdigit()):
            d=d+1
        if(i.upper()):
            u=u+1
        if(i.lower()):
            l=l+1
        if(i=='@' or i=='#' or i=='&'):
            sc=sc+1
    if(d>=1 and u>=1 and l>=1 and sc>=1 and d+u+l+sc>=len(p)):
        print("Password is accepted")
    else:
        print("Password not accepted")
else:
    print("Password length is insufficient")
