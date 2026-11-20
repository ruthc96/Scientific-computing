
# TASK 13: INTERPOLATION

## Objective
To estimate temperatures between known hourly measurements.

## Input Values
Hourly readings are recorded from 8:00 to 13:00.

## Mathematical Operation
Linear interpolation estimates values along straight lines between data points. Cubic spline interpolation uses smooth cubic curves.

## Implementation
SciPy's interp1d() and CubicSpline() are used to estimate intermediate temperatures.

## Output Interpretation
The program estimates the temperature at 10:30 and displays a graph comparing measured values and interpolated curves.

## Parameter Modification
The 10:00 temperature reading is increased from 23°C to 25°C. This changes the estimated temperature at 10:30.

## Real-World Application
Interpolation can estimate missing sensor readings in weather monitoring systems.

## Conclusion
Interpolation estimates unknown values between known measurements.
