import matplotlib.pyplot as plt
import numpy as np
a=np.arange(0,10,0.5)
plt.plot(a,"go:",a*3,"b+-",a*2,"yp-.")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("fourth plot")
plt.show()