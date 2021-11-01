from graphics import *
Win=GraphWin("MIDPOINT CIRCLE",1000,800)
def midPointCircle(c,r):
p=3-2*r
x=0
y=r

plot_circle(x,y,c.x,c.y)

while(x<=y):
x=x+1

if p<0:
p=p+4*x+2
else:
y=y-1
p=p+4*x-4*y+2

plot_circle(x,y,c.x,c.y)
time.sleep(0.01)

def plot_circle(x,y,cx,cy):
pt1=Point(cx+x,cy+y)
pt2=Point(cx-x,cy+y)
pt3=Point(cx+x,cy-y)
pt4=Point(cx-x,cy-y)
pt5=Point(cx+y,cy+x)
pt6=Point(cx-y,cy+x)
pt7=Point(cx+y,cy-x)
pt8=Point(cx-y,cy-x)

pt1.draw(Win)
pt2.draw(Win)
pt3.draw(Win)
pt4.draw(Win)
pt5.draw(Win)
pt6.draw(Win)
pt7.draw(Win)
pt8.draw(Win)

c=Win.getMouse()
r=Win.getMouse()

cx=c.x
cy=c.y
 
rx=r.x
ry=r.y
d=(((rx-cx)**2+(ry-cy)**2)**0.5)
midPointCircle(c,d)
Win.getMouse()


