import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Population growth model
def population_growth(t, y, rate):
    return rate * y

# Initial population and simulation period
initial_population = 100
growth_rate = 0.3
time_span = (0, 10)
time_points = np.linspace(0, 10, 100)

# Solve the differential equation
solution = solve_ivp(
    population_growth,
    time_span,
    [initial_population],
    args=(growth_rate,),
    t_eval=time_points
)

print("Initial population:", initial_population)
print("Population after 10 time units:", solution.y[0, -1])

# Change one input: increase the growth rate
new_rate = 0.4

changed_solution = solve_ivp(
    population_growth,
    time_span,
    [initial_population],
    args=(new_rate,),
    t_eval=time_points
)

print("Population with higher growth rate:",
      changed_solution.y[0, -1])

plt.plot(solution.t, solution.y[0], label="Growth rate 0.3")
plt.plot(changed_solution.t, changed_solution.y[0],
         label="Growth rate 0.4")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Population Growth Using SciPy")
plt.legend()
plt.grid(True)
plt.savefig("task18_scipy_ode.png")
plt.show()
