
# TASK 7: GAUSSIAN ELIMINATION AND LU DECOMPOSITION

## 1. Introduction
Gaussian elimination and LU decomposition are numerical techniques used to solve systems of linear equations.

## 2. Objective
To solve multiple systems using the same coefficient matrix efficiently.

## 3. Input Values
A is a 3 by 3 coefficient matrix. Three different measurement vectors are used.

## 4. Mathematical Operations
The system is represented as Ax = b.
LU decomposition expresses the matrix as triangular factors, which can be reused to solve different systems.

## 5. Implementation
The scipy.linalg library is used. lu_factor() performs the factorization and lu_solve() calculates the solutions.

## 6. Output Interpretation
The program displays the solution for each measurement set and the residual norm. A small residual indicates an accurate solution.

## 7. Changing an Input Parameter
The measurement vector is changed to [18, 10, 10]. This produces a different solution while the coefficient matrix remains unchanged.

## 8. Related Real-World Application
LU decomposition can be used in engineering simulations where the same system structure is solved repeatedly using new measurements.

## 9. Conclusion
LU decomposition saves computation when several systems share the same coefficient matrix.
