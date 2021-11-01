from graphics import*
Win=GraphWin("Ellipse",800,600)
def midPointEllipse(Pt1, rx, ry):
x=0
y=ry

p=((ry**2)-(rx**2*ry)+(rx**2)/4.0)

plot_ellipse(x, y, Pt1.x, Pt1.y)

while(x*ry**2<=y*rx**2):
x=x+1

if(p<0):
p=(p+(2*ry**2*x)+(ry**2))
else:
y=y-1
p=p+(2*ry**2*x)-(2*rx**2*y)+(ry**2)

plot_ellipse(x, y, Pt1.x, Pt1.y)

p=(x+0.5)**2*ry**2+(y-1)**2*rx**2-rx**2*ry**2

while y>=0:
y=y-1

if p<0:
x=x+1
p=p+2*ry**2*x-2*rx**2*y+rx**2
else:
p=p-2*rx**2*y+rx**2

plot_ellipse(x, y, Pt1.x, Pt1.y)

def plot_ellipse(x,y,ex,ey):
pt1=Point(ex+x,ey+y)
pt2=Point(ex+x,ey-y)
pt3=Point(ex-x,ey+y)
pt4=Point(ex-x,ey-y)
pt1.draw(Win)
pt2.draw(Win)
pt3.draw(Win)
pt4.draw(Win)

Pt1=Win.getMouse() #Centre - Point
Pt2=Win.getMouse() #Major Axis End
Pt3=Win.getMouse() #Minor Axis End
rx=(((Pt2.x-Pt1.x)**2+(Pt2.y-Pt1.y)**2)**0.5) #Major Axis
ry=(((Pt3.x-Pt1.x)**2+(Pt3.y-Pt1.y)**2)**0.5) #Minor Axis
midPointEllipse(Pt1, rx, ry)
Win.getMouse()
