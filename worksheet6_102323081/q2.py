import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Sample data: time (t) and velocity (v)
# Replace these with your actual data points
time_data = np.array([0, 1, 2, 3, 4, 5])
velocity_data = np.array([2, 3.1, 7.9, 18.2, 34.3, 56.2])

# Define the quadratic function v(t) = a*t^2 + b*t + c
def quadratic_func(t, a, b, c):
    return a * t**2 + b * t + c

# Use curve fitting to determine the constants a, b, c
params, covariance = curve_fit(quadratic_func, time_data, velocity_data)

# Extract the fitted parameters
a, b, c = params

# Generate fitted curve using the obtained parameters
fitted_velocity = quadratic_func(time_data, a, b, c)

# Plot the original data and fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(time_data, velocity_data, color='red', label='Original Data', marker='o')
plt.plot(time_data, fitted_velocity, label=f'Fitted Curve: v(t) = {a:.2f}t² + {b:.2f}t + {c:.2f}', color='blue')

# Add plot details
plt.title('Velocity vs Time with Quadratic Curve Fitting')
plt.xlabel('Time (t)')
plt.ylabel('Velocity (v)')
plt.legend()
plt.grid(True)
plt.show()