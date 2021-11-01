from graphics import *
def main():
	win = GraphWin("My Window",500,500)
	win.setBackground(color_rgb(255,255,255))
	pt = Point(250,250)
	cir = Circle(pt,50)
	cir.setFill('blue')
	cir.draw(win)
	win.getMouse() #pause for click in window
	win.close()
main()
