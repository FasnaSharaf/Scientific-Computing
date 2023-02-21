a=0
b=1
N=int(input("Enter N:"))
#using for loop
for i in range(N):
    if i==0:
        print(a)
    elif i==1:
        print(b)
    else:
        c=a+b
        print(c)
        a=b
        b=c

#using while loop
i=1
a=0
b=1
while i<=N:
    if i==1:
        print(a)
        i=i+1
    elif i==2:
        print(b)
        i=i+1
    else:
        c=a+b
        print(c)
        a=b
        b=c
        i=i+1