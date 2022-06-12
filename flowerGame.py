#Simple game using random library.

import random

flowers=["lilly","rose","jasmine","lotus"]
print("list is:",flowers)

selection=str(input("Enter your selection:"))
comp_guess=random.randrange(0,3)
guess=flowers[comp_guess]
if selection==guess:
    print("you won")
   
else:
    print("you lost")
print("computer guess:",guess)
print("your selection:",selection)


