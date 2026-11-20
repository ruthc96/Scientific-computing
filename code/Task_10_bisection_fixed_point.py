
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def heat_balance(T):
    return T - 25 - 10 * np.exp(-T / 20)

# Bisection method
solution = root_scalar(
    heat_balance,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-8
)

print("Bisection root:", solution.root)

# Fixed-point iteration: T = 25 + 10 exp(-T/20)
T = 30.0
for i in range(100):
    new_T = 25 + 10 * np.exp(-T / 20)
    if abs(new_T - T) < 1e-8:
        break
    T = new_T

print("Fixed-point root:", T)

# Change initial bracket
modified = root_scalar(
    heat_balance,
    bracket=[25, 45],
    method="bisect"
)

print("Modified bracket root:", modified.root)

x = np.linspace(20, 40, 200)
plt.plot(x, heat_balance(x))
plt.axhline(0)
plt.xlabel("Temperature")
plt.ylabel("Heat balance")
plt.title("Heat Balance Root")
plt.grid()
plt.savefig("task10_bisection.png")
plt.show()
