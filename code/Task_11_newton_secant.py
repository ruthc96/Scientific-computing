
import numpy as np
from scipy.optimize import root_scalar

# Investment cash flows
cash_flows = [-1000, 300, 350, 400, 450]

def npv(rate):
    return sum(
        cash_flows[t] / (1 + rate) ** t
        for t in range(len(cash_flows))
    )

# Newton-Raphson method
newton = root_scalar(
    npv,
    x0=0.1,
    fprime=lambda r: sum(
        -t * cash_flows[t] / (1 + r) ** (t + 1)
        for t in range(1, len(cash_flows))
    ),
    method="newton"
)

# Secant method
secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant"
)

print("Newton-Raphson IRR:", newton.root)
print("Secant IRR:", secant.root)
print("NPV at solution:", npv(newton.root))

# Change initial guess
modified = root_scalar(
    npv,
    x0=0.15,
    fprime=lambda r: sum(
        -t * cash_flows[t] / (1 + r) ** (t + 1)
        for t in range(1, len(cash_flows))
    ),
    method="newton"
)

print("Modified initial guess IRR:", modified.root)
