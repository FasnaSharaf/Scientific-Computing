import numpy as np
import sympy as sym

r=int(input("Enter number of rows/columns"))
A=[]
print("Enter elements row wise")
for i in range(r):
    a=[]
    for j in range(r):
        a.append(int(input()))
    A.append(a)

def eigenvalues(A):
    l=sym.Symbol('l')
    d=np.linalg.det(sym.Matrix((A-(l*np.eye(A.shape[0])))))
    eigenvalues=sym.solve(d==0,l)
    return eigenvalues

print(eigenvalues(A))


def eigenvectors(A, eigenvalues):
    eigenvectors = []
    for eigenvalue in eigenvalues:
        # construct the (A - eigenvalue * I) matrix
        M = A - eigenvalue * np.eye(A.shape[0])

        # form the augmented matrix [M | 0]
        M_aug = sym.Matrix(np.concatenate((M, np.zeros((A.shape[0], 1))), axis=1))

        # solve for the free variables
        free_vars = sym.Matrix(sym.symbols('x0:%d' % A.shape[0]))

        # find the particular solution
        particular = M_aug.LUsolve(sym.Matrix(np.zeros((A.shape[0], 1))))

        # find the general solution
        general = particular + sym.Matrix(free_vars).transpose() * M_aug.nullspace()[0]

        # add the eigenvector to the list
        eigenvectors.append(list(general))

    return eigenvectors
    



