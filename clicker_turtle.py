from turtle import *
from time import sleep
from random import randint, choice

# Черепашка/и
t = Turtle()
t.color('red')
t.shape('circle')
t.speed(0)
t.shapesize(10, 10,)
t.penup()

text = Turtle()
text.color('blue')
text.speed(0)
text.hideturtle()

# перемения/ые
user_click = 0 
user_sila = 1 
user_abdate = 50  
level = 1    

# Саздание функцию/й
def click(x, y):
    global user_click
    user_click += user_sila
    print(f'Кликов: {user_click}')
    update_text()

def update_text():
    text.clear()
    text.penup()
    text.goto(0, 350)
    text.color('yellow')
    text.pendown()
    text.write('🎮 КЛИКЕР-ИГРА 🎮', 
               align='center', 
               font=('Arial', 24, 'bold'))
    
    text.penup()
    text.goto(0, 280)
    text.color('cyan')
    text.pendown()
    text.write(f'🔴 КЛИКОВ: {user_click}', 
               align='center', 
               font=('Arial', 20, 'bold'))
    
    text.penup()
    text.goto(0, 230)
    text.color('lightgreen')
    text.pendown()
    text.write(f'💪 СИЛА КЛИКА: {user_sila}', 
               align='center', 
               font=('Arial', 16, 'bold'))
    
    text.penup()
    text.goto(0, 190)
    text.color('orange')
    text.pendown()
    text.write(f'💰 УЛУЧШЕНИЕ: {user_abdate}', 
               align='center', 
               font=('Arial', 16, 'bold'))
    
    text.penup()
    text.goto(0, 150)
    text.color('pink')
    text.pendown()
    text.write(f'📈 УРОВЕНЬ: {level}', 
               align='center', 
               font=('Arial', 16, 'bold'))
    
    text.penup()
    text.goto(0, 110)
    text.color('gray')
    text.pendown()
    text.write('⌨️ Нажми E - УЛУЧШИТЬ', 
               align='center', 
               font=('Arial', 12))
    
    scr.update()

def abdeit():
    global user_click, user_abdate, user_sila, level
    
    if user_click >= user_abdate:

        user_click -= user_abdate
        
        user_sila += 5
        
        user_abdate += 50
        
        level += 1
        
        t.color('gold')
        t.shapesize(12, 12, 10)
        scr.update()
        sleep(0.2)
        t.color('red')
        t.shapesize(10, 10, 10)

        text.penup()
        text.goto(0, -200)
        text.color('red')
        text.pendown()
        write('Уровень поднят', 
               align='center', 
               font=('Arial', 12))
    
        
        print(f'🎉 УЛУЧШЕНИЕ! Уровень: {level} | Сила: {user_sila}')
        update_text()
        
    else:
        need = user_abdate - user_click
        print(f'❌ Нужно еще {need} кликов!')

scr = Screen()
scr.setup(800, 600)
scr.bgcolor('#1a1a1a')
scr.title('🎮 КЛИКЕР-ИГРА 🎮')
scr.tracer(0)
update_text()
# Работа с кликоми и клавиатурой
t.onclick(click)
scr.onkey(abdeit, 'e')
scr.onkey(abdeit, 'E')
scr.listen()


done()
