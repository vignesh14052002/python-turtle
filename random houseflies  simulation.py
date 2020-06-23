import turtle,random

z=['0','1','2','3','4','5','6','7','8','9']
z.extend(['a','b','c','d','e','f'])
def chooseclr(a):
	global z
	cl='#'
	for i in range(6):
		d=random.choice(z)
		cl+=d
	a.color(cl)


def positions(a):
	a.speed(0)
	#chooseclr(a)  #uncomment if you want different colours
	a.pu()
	a.setpos(random.randint(-400,400),random.randint(-400,400))
	a.pd()
def move(a):
	a.pu()#comment if you want path
	#a.speed(random.randint(0,10))#uncomment if you want different speeds
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
li=[]
for i in range(50):#number of turtles
	li.append(turtle.Turtle())


for i in li:
	positions(i)#comment these if you want same positions



for i in range(random.randint(100,500)):
	for j in li:
		move(j)
		


turtle.done()