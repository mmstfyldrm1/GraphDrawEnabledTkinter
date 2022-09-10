import random
import matplotlib.pyplot as plt

xAxis=[]
yAxis=[]
plt.figure()

def RandomNumber():
    x=random.random()
    y=random.random()
    xAxis.append(x)
    yAxis.append(y)
i=0
while(i<5):
    RandomNumber()
    i=i+1




plt.subplot(2,2,1)
plt.plot(xAxis,yAxis,'r')
plt.title("Graph 1")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
RandomNumber()

plt.subplot(2,2,2)
plt.plot(xAxis,yAxis,'r')
plt.title("Graph 2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
RandomNumber()




plt.subplot(2,1,2)
plt.plot(xAxis,yAxis,'bo-')
plt.title("Graph 3")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
RandomNumber()


plt.tight_layout()
plt.show()








