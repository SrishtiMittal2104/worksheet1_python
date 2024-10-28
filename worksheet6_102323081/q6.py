import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def f(x):
    return x**4 - 3*x**3 + 2


result = minimize(f, 0.5)

local_min_x = result.x[0]
local_min_y = f(local_min_x)

print(f"Local minimum is at x = {local_min_x}, f(x) = {local_min_y}")

x = np.linspace(-2, 3, 400)
y = f(x)

plt.plot(x, y, color='blue')
plt.scatter(local_min_x, local_min_y, color='red', zorder=5, label='Local Minima')
plt.text(local_min_x, local_min_y, f'({local_min_x:.2f}, {local_min_y:.2f})', fontsize=10, verticalalignment='bottom', horizontalalignment='right')
plt.legend()
plt.show()
