import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,2*np.pi,num=1200)
a=np.sin(2*np.pi*t)
np.savetxt("test.csv",np.column_stack([t,a]),delimiter=',')
csv=np.genfromtxt("test.csv",delimiter=',')
print(csv)

plt.hist(csv[:,1],bins=10)
plt.xlabel('amplitude')
plt.ylabel('Frequency')
plt.show()

mean=np.sum(a)/len(a)
print(mean, np.mean(a))

std = np.sqrt(np.sum((a-mean)**2) / (len(a)-1))
print(std,np.std(a,ddof=1))
