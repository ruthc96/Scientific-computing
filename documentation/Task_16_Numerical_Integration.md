# Task 16: Numerical Integration

## Objective
To estimate total electrical energy consumption from power measurements over time.

## Input Data
Time is measured in hours:
0, 1, 2, 3, 4 and 5.

Power consumption is measured in kilowatts:
2, 3, 4, 5, 4 and 3.

## Mathematical Operation
Numerical integration estimates the area under a curve.

The program uses Simpson's rule through SciPy's simpson function.

Energy is calculated by integrating power with respect to time. The result is measured in kilowatt-hours (kWh).

## Output and Interpretation
The program displays the estimated energy consumed during the five-hour period.

A higher area under the power-time curve means greater total energy consumption.

## Changed Input
Power measurements are increased by 20%. The estimated energy consumption also increases by 20%.

## Real-World Application
A household or company can estimate electricity consumption from power readings collected at regular intervals.

Assumption: The measurements represent the power consumption throughout the intervals between readings.
