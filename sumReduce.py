#To find sum of elements in list using reduce fuction.

from functools import reduce
list1=[5,7,3,1,4]
result=reduce(lambda x1,x2:x1+x2,list1)
print(result)
