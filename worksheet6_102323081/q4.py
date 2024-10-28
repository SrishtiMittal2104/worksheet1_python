import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f(x):
    return 3*x**3 - 5*x**2 + 2*x - 8

root1 = optimize.root(f,1)
root2 = optimize.root(f,2)
root3 = optimize.root(f,3)

roots = [root1, root2, root3]

xvals = np.linspace(-3,3,100)
yvals = f(xvals)
# print(xvals)

plt.plot(xvals, yvals)
plt.show()