
import turtle
a=turtle.Turtle()
a.speed(0)
def changepos(i,j):
	a.pu()
	a.setpos(-700+i,200-j)
	a.pd()
def polygon(n):#number of sides
	for i in range(n):
		a.forward(70)
		a.left(360/n)
m,n=0,0
for i in range(3,12):
	changepos(m,n)
	polygon(i)
	m+=300
	if m>600:
		m=0
		if a.pos()==(-100,200):
			n+=200
		else:
			n+=300
	
turtle.done()

#author @_._hello_world._._


