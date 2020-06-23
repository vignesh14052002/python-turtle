import turtle,random

def petal(a,f,c):
    a.fillcolor(c)
    a.begin_fill()
    for i in range(5):
        a.forward(f)
        a.left(11)
    a.circle(f,180)
    a.lt(145)
    a.circle(f,180)
    for i in range(5):
        a.forward(f)
        a.left(10.5)
    
    
    a.end_fill() 
def stem(a):
    global p
    a.setheading(270)
    a.fillcolor('green')
    a.begin_fill()
    curve(a,60,10,5)
    a.setheading(0)
    p=a.ycor()
    a.forward(10)
    a.setheading(130)
    curve(a,60,10,5,right=True)
    a.rt(150)
    a.end_fill()

def curve(a,b,c,d,right=False):
    for i in range(d):
        a.forward(b)
        if right==False:
            a.lt(c)
        else:
            a.rt(c)
def soil(a):
    a.fillcolor('brown')
    a.begin_fill()
    a.setheading(180)
    for i in range(2):
        a.forward(2000)
        a.lt(90)
        a.forward(100)
        a.lt(90)
    a.end_fill()
def leaf(a,b,c,d):
    
    a.fillcolor('green')
    a.begin_fill()
    curve(a,b,c,d//2)
    curve(a,b,c+5,d,right=True)
    a.rt(75)
    curve(a,b,c+5,d,right=True)
    a.lt(90)
    curve(a,b,c,d//2,right=True)
    a.end_fill()
def grass(a,b,c,d):
    for i in range(3):
        a.fillcolor('green')
        a.begin_fill()
        a.setheading(90)
        curve(a,b,c,d)
        a.lt(175)
        curve(a,b+b//4,c+c//3,d-1,right=True)
        a.end_fill()
        a.begin_fill()
        a.setheading(90)
        curve(a,b,c,d,right=True)
        a.rt(175)
        curve(a,b+b//4,c+c//3,d-1)
        a.end_fill()
        c-=4
a=turtle.Turtle()
a.speed(0)
stem(a)
for i in range(5):
    petal(a,30,'red')
    a.lt(180)
a.lt(90)
a.fillcolor('yellow')
a.begin_fill()
a.speed(0)
a.circle(60,355)
a.rt(100)

a.end_fill()
a.pu()
a.rt(7)
curve(a,60,10,4)
a.pd()
a.lt(60)
leaf(a,20,10,7)
a.pu()
a.setpos(a.xcor()+1000,p)
a.pd()
soil(a)

for i in range(100):
    a.pu()
    a.setpos(random.randint(-1000,1000),p-random.randint(0,60))
    a.pd()
    grass(a,10,15,7)

turtle.done()


