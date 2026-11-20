# Task 18: Numerical Solution of ODEs Using SciPy

## 1. Objective
To solve an ordinary differential equation (ODE) numerically using SciPy's `solve_ivp` function.

## 2. Real-World Application
This task models the charging of a capacitor in an RC electrical circuit.

## 3. Mathematical Model
The charging equation is:

dV/dt = (Vs - V)/(R*C)

Where:
- Vs = Supply voltage (5.0 V)
- R = Resistance (1000 ohms)
- C = Capacitance (0.001 F)
- V0 = Initial capacitor voltage (0.0 V)

## 4. Inputs and Operations
The program uses NumPy to create time points and SciPy's `solve_ivp` to solve the differential equation from 0 to 5 seconds.

It also calculates the exact solution:

V(t) = Vs * (1 - exp(-t/(R*C)))

The numerical and exact solutions are compared to determine the maximum error.

## 5. Results
- Solver success: True
- Capacitor voltage after 5 seconds: approximately 4.9663 V.
- The numerical solution closely follows the exact solution.
- The maximum error is very small.

## 6. Interpretation
The capacitor voltage increases over time as it charges. It gradually approaches the supply voltage of 5 V. The graph shows that the numerical solution agrees closely with the exact solution.

## 7. Parameter Variation
If the capacitance is increased from 0.001 F to 0.002 F, the time constant increases from 1 second to 2 seconds. This makes the capacitor charge more slowly. After 5 seconds, its voltage would be approximately 4.5896 V instead of 4.9663 V.

## 8. Conclusion
SciPy's `solve_ivp` successfully solves the RC circuit charging equation. Comparing the numerical and exact solutions demonstrates the accuracy of the numerical method.
