import numpy as np
import matplotlib.pyplot as plt

age1=np.array([10,20,30])
num1=np.array([100,200,300])
age2=np.array([20,30,40])
num2=np.array([200,300,400])
np.savetxt("file1.csv",np.column_stack([age1,num1]),delimiter=',')
np.savetxt("file2.csv",np.column_stack([age2,num2]),delimiter=',')
file1=np.genfromtxt("file1.csv",delimiter=',')
file2=np.genfromtxt("file2.csv",delimiter=',')

a1=file1[:,0]
a2=file2[:,0]

result=[]
for a,n in file1:
    flag=0
    for a1,n1 in file2:
        if a==a1:
            result.append([a,n+n1])
            flag=1
            break
    if flag==0:
        result.append([a,n])

for a1,n1 in file2:
    flag=0
    for a,n in file1:
        if a==a1:
            flag=1
    if flag==0:
        result.append([a1,n1])

result=np.array(result)
print(result)

plt.hist(result[:,1], bins=4)
plt.title("Histogram of merged data")
plt.xlabel("Age")
plt.ylabel("Number of students")
plt.show()

        