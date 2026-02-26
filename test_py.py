from turtle import *

t1 = Turtle()
t1.color('red')
t1.shape('turtle')
t1.penup()
t1.goto(0, 50)
t1.pendown()

t2 = Turtle()
t2.color('green')
t2.shape('turtle')
t2.penup()
t2.goto(0, -50)
t2.pendown()

for i in range(80):
    t1.forward(i)
    t2.forward(i)
    t1.left(89.99)
    t2.left(89.99)
