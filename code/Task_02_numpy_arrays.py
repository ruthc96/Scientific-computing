
import numpy as np

# 24 hourly temperature readings in degrees Celsius
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Convert all readings to Fahrenheit
temperatures_f = 1.8 * temperatures_c + 32

print("Daily mean temperature:", round(mean_temp, 2), "C")
print("Minimum temperature:", min_temp, "C")
print("Maximum temperature:", max_temp, "C")
print("First six Fahrenheit readings:", temperatures_f[:6])

# Modified input: increase every reading by 2 degrees
modified_temperatures = temperatures_c + 2

print("New mean after increasing readings by 2 C:",
      round(np.mean(modified_temperatures), 2), "C")
