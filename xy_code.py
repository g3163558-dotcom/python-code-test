from turtle import *
from time import sleep



t = Turtle()
t.speed(0)
t.shape("turtle")
t.color("#c4e6e9")

def click_user(x, y):
    print(f'Кординаты: x={x:.1f}  y={y:.1f}')

    t.goto(x, y)
    for i in range(4):
        t.forward(6)
        t.left(90)
    
    t.penup()
    t.left(45)
    t.forward(4)
    t.pendown()
def hill():
    t.clear()

scr = t.getscreen()
scr.listen()
scr.onclick(click_user)
scr.onkey(hill, 'c')

while True:
    scr.update()
    print('Стереть всё на бинд: [c]')
    sleep(10)
