import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np



x=np.arange(1,10,2) # x-axis number
y= np.arange(2,12,2) #y-axis number

x1 = np.arange(1,2,0.1)
y1 = np.arange(1,2,0.1)

x2 = np.arange(2,3,0.1)
y2 = np.arange(3,4,0.1)


fig = Figure(figsize=plt.figaspect(1), dpi=100) #graph widh and resolution



plt.subplot(2,2,1)
fig.add_subplot(111)
plt.title("Graph-1")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y,"r-")
#plt.axis([1,5,1,4]) #x-axis min and max y-axis min and max


plt.subplot(2,2,3)
fig.add_subplot(111)
plt.title("Graph-2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x1,y1)
#plt.axis([1,5,1,4]) #x-axis min and max y-axis min and max


plt.subplot(1,2,2)
fig.add_subplot(111)
plt.title("Graph-3")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x2,y2,x,"b-")
plt.legend(['w=1','w=2']) #information area
#plt.axis([1,5,1,4]) #x-axis min and max y-axis min and max

plt.tight_layout() #Numbers improve position
plt.savefig('grafik.png') # saves the graphic to the specified file path
plt.show()





