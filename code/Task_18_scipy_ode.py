import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Task 18: Numerical Solution of ODEs Using SciPy
# Real-world application: Charging of an RC electrical circuit

Vs = 5.0
R = 1000.0
C = 0.001
V0 = 0.0

def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]

t_eval = np.linspace(0, 5, 200)

solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

if not solution.success:
    raise RuntimeError(solution.message)

exact = Vs * (1 - np.exp(-solution.t / (R * C)))
maximum_error = np.max(np.abs(solution.y[0] - exact))

print("Task 18: RC Circuit Charging")
print("Solver success:", solution.success)
print(f"Supply voltage: {Vs:.2f} V")
print(f"Resistance: {R:.0f} ohms")
print(f"Capacitance: {C:.3f} F")
print(f"Initial voltage: {V0:.2f} V")
print(f"Capacitor voltage at 5 seconds: {solution.y[0, -1]:.4f} V")
print(f"Exact voltage at 5 seconds: {exact[-1]:.4f} V")
print(f"Maximum error: {maximum_error:.3e} V")

plt.figure(figsize=(9, 5))
plt.plot(solution.t, solution.y[0], label="Numerical solution (solve_ivp)")
plt.plot(solution.t, exact, "--", label="Exact solution")
plt.xlabel("Time (seconds)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC Circuit Charging")
plt.legend()
plt.grid(True)
plt.savefig("task18_scipy_ode.png", dpi=300, bbox_inches="tight")
plt.show()
