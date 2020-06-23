
import turtle
a=turtle.Turtle()
a.speed(0)
def changepos(i,j):
	a.pu()
	a.setpos(-700+i,200-j)
	a.pd()
def polygon_spiral(n,k):#number of sides
	l=0
	c=a.xcor()
	while c-a.xcor()<100:
		a.forward(l)
		a.left(360/n)
		l+=k
m,n=0,0
for i in range(3,12):
	changepos(m,n)
	polygon_spiral(i,12-i)
	m+=300
	if m>600:
		m=0
		if a.pos()==(-100,200):
			n+=200
		else:
			n+=300
	
turtle.done()

#author @_._hello_world._._


