x=input("enter the string:")
is_palindrome=False
i=0
while(x[i]==x[-(i+1)]):
    i=i+1
    if i>(len(x)/2 +1):
        is_palindrome=True
        break
if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")
    
        
    