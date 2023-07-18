from turtle import forward, right, left
from turtle import exitonclick, shape, goto, penup, pendown
from math import sqrt
from random import randint
import random

shape("turtle")
penup()
goto(-375,-150)
pendown()

def domecek(a):
    c = sqrt (2*(a**2))

    left(45)
    forward(c)

    right(45+90)
    forward(a)

    right(90)
    forward(a)

    right(90)
    forward(a)

    right(90)
    forward(a)

    left(45+90)
    forward(c/2)

    left(90)
    forward(c/2)

    left(90)
    forward(c)
    
    left(45)
    penup()
    forward(20)
    pendown()    

for i in range(5):
    domecek(random.randint(50,150))

exitonclick()