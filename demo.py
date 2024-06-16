import turtle as t
import randomcolor as r
t.speed(1000)
t.penup()
t.goto(0,100)
t.pendown()
for i in range(100):	
	c= r.RandomColor().generate()
	t.color(f"{c[0]}")
	
	t.begin_fill()
	t.circle(40);
	t.right(4);
	t.forward(10);
	t.end_fill()
	
t.done()
