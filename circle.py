import matplotlib.pyplot as plt
plt.xlabel("x")
plt.ylabel("y")
circle=plt.Circle((0,0),1.5,fc='blue',ec='red')
plt.gca().add_patch(circle)
plt.axis('scaled')
plt.show()