import matplotlib.pyplot as plt
#plt.plot([1,2,3,4,5])
# x is optional. line width and marksize is same
#plt.plot([1,2,3,4,5],'r-',markersize=20)
#plt.plot([4,6,7,8,9],'r+',linewidth=20)
plt.plot([10,20,30,40,50],"g",[5,10,20,30],"r")




plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("First plot")

plt.show()