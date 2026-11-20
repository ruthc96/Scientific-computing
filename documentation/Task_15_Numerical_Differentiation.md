# Task 15: Numerical Differentiation

## Objective
To estimate the velocity of a moving object from measured position data.

## Input Data
The program uses time measurements in seconds:
0, 1, 2, 3, 4 and 5.

The corresponding positions are:
0, 3, 8, 15, 24 and 35 metres.

## Mathematical Operation
Velocity is the rate of change of position with respect to time.

The program uses NumPy's gradient function to approximate the derivative numerically.

## Output and Interpretation
The program displays the estimated velocity at each time measurement.

The graph shows how velocity changes as time increases. The increasing velocity indicates that the object is moving faster.

## Changed Input
The program uses a second set of measurements with half-second intervals. This changes the sampling interval and produces new velocity estimates.

## Real-World Application
Numerical differentiation can estimate the speed of a vehicle using position readings collected by GPS.

Assumption: Position measurements are sufficiently accurate. Measurement noise can affect numerical derivative estimates.
