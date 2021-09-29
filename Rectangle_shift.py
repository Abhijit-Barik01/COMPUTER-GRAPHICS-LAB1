import matplotlib.pyplot as plt
p=[0,0,0,0,0]
q=[0,0,0,0,0]
tx=5
ty=4
#x axis
x=[1,1,5,5,1]
#y axis
y=[1,5,5,1,1]
for i in range(5):
  p[i]=x[i]+tx
  q[i]=y[i]+ty
plt.plot(x,y)
plt.plot(p,q)
plt.title('Rectangle')
plt.show()