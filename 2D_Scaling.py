from graphics import *
choice=int(input(("Enter your choice:\n1.Line\n2.Rectangle\n3.Polygon\n4.Circle\n5.Ellipse\n__")))
Win=GraphWin("Scaling",1400,900)
pt1=Win.getMouse()
pt2=Win.getMouse()
if choice == 1:
L1=Line(pt1,pt2)
L1.draw(Win)
if choice == 2:
L1=Rectangle(pt1,pt2)
L1.draw(Win)
if choice == 3:
L1=Polygon(pt1,pt2)
L1.draw(Win)
if choice == 4:
rad=(((pt2.x-pt1.x)**2)+((pt2.y-pt1.y)**2))**0.5
L1=Circle(pt1,rad)
L1.draw(Win)
if choice == 5:
L1=Oval(pt1,pt2)
L1.draw(Win)
sx=float(input(("Enter scaling factor: sx = ")))
sy=float(input(("Enter scaling factor: sy = ")))
def Scale(sx,sy):
newx1=pt2.x+(pt1.x-pt2.x)*sx
newy1=pt2.y+(pt1.y-pt2.y)*sy
New_pt1=Point(newx1,newy1)
if choice == 1:
L1=Line(New_pt1,pt2)
L1.draw(Win)
if choice == 2:
L1=Rectangle(New_pt1,pt2)
L1.draw(Win)
if choice == 3:
L1=Polygon(New_pt1,pt2)
L1.draw(Win)
if choice == 4:
rad=(((pt2.x-New_pt1.x)**2)+((pt2.y-New_pt1.y)**2))**0.5
L1=Circle(New_pt1,rad)
L1.draw(Win)
if choice == 5:
L1=Oval(New_pt1,pt2)
L1.draw(Win)

Scale(sx,sy)
Win.getMouse()
