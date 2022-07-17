#To find the largest element in a list using reduce function.

from functools import reduce
a=[4,5,8,1,2]
result=reduce(lambda x1,x2:x1 if x1>x2 else x2,a)
print(result)