import matplotlib.pyplot as plt;
x=[2,2,4,4,2];
y=[2,4,4,2,2];
fig,ax=plt.subplots()
ax.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Triangle draw")
plt.show()