import turtle,random
a=turtle.Turtle()
a.pu()
a.setpos(random.randint(-400,400),random.randint(-400,400))
a.pd()
for i in range(random.randint(100,500)):
	a.speed(random.randint(0,10))
	x=random.randint(0,100)
	y=random.randint(0,360)
	if random.randint(0,1):
		if random.randint(0,1):
			a.forward(x)
		else:
			a.backward(x)
	else:
		if random.randint(0,1):
			a.left(y)
		else:
			a.right(y)
turtle.done()