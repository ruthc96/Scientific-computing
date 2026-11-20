
# TASK 8: ITERATIVE METHODS FOR LINEAR SYSTEMS

## 1. Introduction
Iterative methods solve linear systems by repeatedly improving an initial estimate.

## 2. Objective
To compare the Jacobi and Gauss-Seidel methods using a temperature model.

## 3. Input Values
A five-point temperature model is represented by a coefficient matrix and a boundary vector.

## 4. Mathematical Operations
The program uses repeated numerical updates until the difference between estimates is smaller than the selected tolerance.

## 5. Implementation
Python and NumPy implement the Jacobi and Gauss-Seidel methods. Matplotlib plots their convergence.

## 6. Output Interpretation
The solutions estimate temperatures at five interior points. The convergence graph shows how the error decreases with each iteration.

## 7. Changing an Input Parameter
The left boundary value is increased from 100 to 120 degrees. The resulting temperature estimates change because the boundary condition has changed.

## 8. Related Real-World Application
Iterative methods can estimate temperatures in buildings, electrical networks and engineering systems.

## 9. Conclusion
Jacobi and Gauss-Seidel methods provide ways of solving linear systems through repeated approximations.
