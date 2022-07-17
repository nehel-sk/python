#Add two lists using map and lambda

list1=[1,2,3,4]
list2=[4,5,6,7]
result=map(lambda x1,x2:x1+x2,list1,list2)
print(list(result))
