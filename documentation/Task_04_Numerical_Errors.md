
# TASK 4: FLOATING-POINT ARITHMETIC AND NUMERICAL ERRORS

## 1. Introduction
This task explores floating-point arithmetic and numerical errors in computer calculations.

## 2. Objective
To demonstrate how computers represent decimal numbers and how approximation affects numerical accuracy.

## 3. Input Values
The program uses 0.1, 0.2, 0.3 and the approximate value of the square root of 2.

## 4. Mathematical Operations
- Addition of floating-point numbers.
- Absolute error = |True value - Approximate value|.
- Relative error = Absolute error / |True value|.
- NumPy isclose() compares values within a numerical tolerance.

## 5. Implementation
Python and NumPy are used to compare floating-point values and calculate absolute and relative errors.

## 6. Output Interpretation
The exact comparison between 0.1 + 0.2 and 0.3 may return False because decimal numbers can have approximate binary representations. The tolerance-based comparison provides a more suitable way to compare these values.

## 7. Changing an Input Parameter
The approximation is changed from 1.414 to 1.4142. The new approximation is closer to the square root of 2, reducing the absolute error.

## 8. Related Real-World Application
Floating-point accuracy is important in financial calculations, engineering simulations and GPS/navigation systems where small numerical errors can affect results.

## 9. Conclusion
The task demonstrates that floating-point calculations may contain small errors and that suitable numerical tolerances help improve comparisons.
