N=int(input("Enter N:"))

#without recursion
i=1
fact=1
if N==0:
    print(1)
else:
    while i<=N:
        fact=fact*i
        i=i+1
    print(fact)

#with recursion
def factorial(N):
    if N==0 or N==1:
        return 1
    else:
        return (N*factorial(N-1))
print(factorial(N))
