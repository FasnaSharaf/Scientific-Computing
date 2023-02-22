import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f(t):
    return 4 * t ** 2 + 3

#limits of integration
a = 0
b = 2

#number of intervals for numerical integration
N = 100

# Trapezoidal rule
p = np.linspace(a, b, N+1)
y = f(p)
area_trap = np.trapz(y, p)
print("Trapezoidal rule: ", area_trap)

# Simpson's rule
p = np.linspace(a, b, 2*N+1)
y = f(p)
area_simpson = integrate.simps(y, p)
print("Simpson's rule: ", area_simpson)

# Analytical solution
area_analytical = integrate.quad(f, a, b)[0]
print("Analytical solution: ", area_analytical)

# Error calculation
error_trap = np.abs(area_trap - area_analytical)
error_simpson = np.abs(area_simpson - area_analytical)

# Print the errors
print("Trapezoidal rule error: ", error_trap)
print("Simpson's rule error: ", error_simpson)