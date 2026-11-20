# Task 17: Ordinary Differential Equations – Euler Method

## Objective
To approximate how the temperature of a hot object changes as it cools toward room temperature.

## Input Data
- Initial temperature: 90°C
- Room temperature: 25°C
- Cooling rate: 0.2
- Time step: 0.5 minutes
- Total simulation time: 10 minutes

## Mathematical Operation
The cooling process is represented by:

dT/dt = -k(T - Tr)

Where:
- T is the object's temperature.
- Tr is room temperature.
- k is the cooling rate.

Euler's method estimates the next temperature using:

T(next) = T(current) + step × rate of change

## Output and Interpretation
The program estimates the object's temperature at each time step.

The graph shows the temperature decreasing toward room temperature as time passes.

## Changed Input
The cooling rate is increased from 0.2 to 0.3. The object cools faster and reaches a lower temperature within the same simulation period.

## Real-World Application
This model can estimate how quickly food, machinery or heated equipment cools.

Assumption: Room temperature and the cooling-rate parameter remain constant during the simulation.
