import matplotlib.pyplot as plt
m=[]
n=[]
p=[]
q=[]
def ROUND(a):
  return int(a+.5)

def drawDDA(x1,y1,x2,y2):
  x,y=x1,y1
  length=(x2-x1) if (x2-x1)>(y2-y1) else (y2-y1)
  dx=(x2-x1)/float(length)
  dy=(y2-y1)/float(length)
  print('x=%s,y=%s' %(ROUND(x),ROUND(y)))
  for i in range(length):
    x+=dx
    y+=dy
    m.insert(i,ROUND(x))
    p.insert(i,ROUND(x+5))
    n.insert(i,ROUND(y))
    q.insert(i,ROUND(y+4))
    print('x=%s,y=%s' %(ROUND(x),ROUND(y)))

  plt.plot (m,n)
  plt.plot(p,q)
  print('x=%s,y=%s' %(ROUND(x),ROUND(y)))

  plt.plot(m,n)
  plt.plot(m,n)
  plt.show()
drawDDA(2,5,10,20)
