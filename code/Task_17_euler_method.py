import numpy as np
import matplotlib.pyplot as plt

# Model: cooling of an object toward room temperature
room_temperature = 25.0
initial_temperature = 90.0
cooling_rate = 0.2

# Time settings
step = 0.5
total_time = 10
time = np.arange(0, total_time + step, step)

# Euler's method
temperature = np.zeros(len(time))
temperature[0] = initial_temperature

for i in range(len(time) - 1):
    rate = -cooling_rate * (temperature[i] - room_temperature)
    temperature[i + 1] = temperature[i] + step * rate

print("Temperature after 10 minutes:", temperature[-1])

# Change one input: use a higher cooling rate
faster_rate = 0.3
faster_temperature = np.zeros(len(time))
faster_temperature[0] = initial_temperature

for i in range(len(time) - 1):
    rate = -faster_rate * (faster_temperature[i] - room_temperature)
    faster_temperature[i + 1] = faster_temperature[i] + step * rate

print("Temperature with faster cooling:", faster_temperature[-1])

plt.plot(time, temperature, marker="o", label="Original cooling rate")
plt.plot(time, faster_temperature, label="Faster cooling rate")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Cooling Model Using Euler's Method")
plt.legend()
plt.grid(True)
plt.savefig("task17_euler_method.png")
plt.show()
