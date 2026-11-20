
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# Hourly temperature readings
hours = np.array([8, 9, 10, 11, 12, 13], dtype=float)
temperature = np.array([20, 21, 23, 24, 26, 27], dtype=float)

# Linear interpolation
linear = interp1d(hours, temperature)

# Cubic spline interpolation
spline = CubicSpline(hours, temperature)

new_hours = np.arange(8, 13.1, 0.5)

linear_values = linear(new_hours)
spline_values = spline(new_hours)

print("Estimated temperature at 10:30:")
print("Linear:", float(linear(10.5)))
print("Cubic spline:", float(spline(10.5)))

# Change one input reading
modified_temperature = temperature.copy()
modified_temperature[2] = 25

modified_linear = interp1d(hours, modified_temperature)
print("Modified estimate at 10:30:",
      float(modified_linear(10.5)))

plt.plot(hours, temperature, "o", label="Measured")
plt.plot(new_hours, linear_values, label="Linear")
plt.plot(new_hours, spline_values, label="Cubic spline")
plt.xlabel("Hour")
plt.ylabel("Temperature (C)")
plt.title("Temperature Interpolation")
plt.legend()
plt.grid()
plt.savefig("task13_interpolation.png")
plt.show()
