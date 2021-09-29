import matplotlib.pyplot as plt

plt.plot([2,6,7,8,9],"r*-",markersize=20)
plt.plot([2,3,5,7,6],"gp-")
plt.plot([1,2,4,5])
plt.plot([2,4,9,5],"bo--",[6,10,11,13],"<")

#"ro-" means colour ,marker, line
# marker are -.,o,h,<,>,1,2,3,4,s,p,h,*,+.x,D,d,|
#color means b=black,g=green,r=red,c=cyan,y=yelllow,w=white
# line style means --,-,-.,:,
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("third plot")
plt.show()
