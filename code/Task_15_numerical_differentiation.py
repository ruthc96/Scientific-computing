import numpy as np
import matplotlib.pyplot as plt

# Time in seconds and measured position in metres
time = np.array([0, 1, 2, 3, 4, 5], dtype=float)
position = np.array([0, 3, 8, 15, 24, 35], dtype=float)

# Estimate velocity using numerical differentiation
velocity = np.gradient(position, time)

print("Time:", time)
print("Position:", position)
print("Estimated velocity:", velocity, "m/s")

# Change one input: use a smaller time interval
new_time = np.array([0, 0.5, 1, 1.5, 2], dtype=float)
new_position = new_time ** 2 + 2 * new_time
new_velocity = np.gradient(new_position, new_time)

print("\nChanged time measurements:")
print("Time:", new_time)
print("Position:", new_position)
print("Estimated velocity:", new_velocity, "m/s")

plt.plot(time, velocity, marker="o", label="Estimated velocity")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity Estimated from Position Data")
plt.legend()
plt.grid(True)
plt.savefig("task15_differentiation.png")
plt.show()
