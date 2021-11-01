import math
from graphics import *

Win=GraphWin("Rotation", 800, 800)

pt1=Win.getMouse()
pt2=Win.getMouse()
L1=Line(pt1,pt2)
L1.draw(Win)

deg_angle=float(input(("Enter the angle of rotation:")))

def Rotate(deg, L):
rad_angle=(deg*3.14)/180

new_ptx=pt2.x+(pt1.x-pt2.x)*math.cos(rad_angle)-(pt1.y-pt2.y)*math.sin(rad_angle)
new_pty=pt2.y+(pt1.x-pt2.x)*math.sin(rad_angle)+(pt1.y-pt2.y)*math.cos(rad_angle)
New_pt1=Point(new_ptx, new_pty)

L.undraw()
L2=Line(New_pt1,pt2)
L2.draw(Win)
time.sleep(0.05)

return L2

def Animate():
i=5.0
L=L1
while i<deg_angle :
time.sleep(0.05)
L=Rotate(i,L)
i=i+5

L=Rotate(deg_angle,L)
Win.getMouse()

Animate()
