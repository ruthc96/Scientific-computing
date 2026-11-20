
# TASK 11: NEWTON-RAPHSON AND SECANT METHODS

## Objective
To estimate the internal rate of return of an investment.

## Input Values
The cash flows are -1000, 300, 350, 400 and 450 over five periods.

## Mathematical Operation
Net present value is calculated using NPV = sum of CF(t)/(1+r)^t. The root is the rate where NPV equals zero.

## Implementation
SciPy's root_scalar() applies Newton-Raphson and Secant methods.

## Output Interpretation
The estimated roots represent the investment's internal rate of return. The NPV at the estimated root should be close to zero.

## Parameter Modification
The initial guess for Newton-Raphson is changed from 0.10 to 0.15. The final estimate should remain close if both guesses converge to the same root.

## Real-World Application
These methods help investors evaluate project profitability and investment returns.

## Conclusion
Newton-Raphson and Secant methods can efficiently approximate roots of financial equations.
