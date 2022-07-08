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
