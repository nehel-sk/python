#Turtle program to print a polygon

import turtle as t
h=t.Turtle()

num_sides=int(input("enter the number of sides:"))
side_len=int(input("enter the length of each side:"))
angle=360.0/num_sides

for i in range(num_sides):
    h.forward(side_len)
    h.right(angle)
t.done()
