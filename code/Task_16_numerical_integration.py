import numpy as np
from scipy.integrate import simpson

# Time in hours and power consumption in kilowatts
time = np.array([0, 1, 2, 3, 4, 5], dtype=float)
power = np.array([2, 3, 4, 5, 4, 3], dtype=float)

# Estimate total energy using Simpson's rule
energy = simpson(power, x=time)

print("Estimated energy consumption:", energy, "kWh")

# Change one input: increase power consumption by 20%
increased_power = power * 1.2
new_energy = simpson(increased_power, x=time)

print("Energy after 20% increase:", new_energy, "kWh")

print("Difference:", new_energy - energy, "kWh")
