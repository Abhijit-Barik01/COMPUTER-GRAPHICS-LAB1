from graphics import *
Win=GraphWin("DDA Line Drawing Algo",1000,600)
def DDA_Line(pt1,pt2):
	dy=pt2.y-pt1.y
	dx=pt2.x-pt1.x
	x=pt1.x
	y=pt1.y
	s=0
	if dy>dx:
		s=dy
	else:
		s=dx	
	x_inc=dx/s
	y_inc=dy/s
	try:
		pt1.draw(Win)
	except:
	 	pass
	for i in range (int(s)):
		x+=x_inc
		y+=y_inc
		x_r=int(x+0.5)
		y_r=int(y+0.5)
		pt=Point(x_r,y_r)
		pt.draw(Win)
ch=1
while (ch):
	Pt1=Win.getMouse()
	Pt2=Win.getMouse()
	DDA_Line(Pt1, Pt2)
Win.getMouse()