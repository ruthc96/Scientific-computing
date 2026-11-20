
# TASK 6: SOLUTION OF SYSTEMS OF LINEAR EQUATIONS

## 1. Introduction
Linear equations can represent real-world problems involving several unknown quantities.

## 2. Objective
To solve simultaneous equations using NumPy.

## 3. Input Values
Type A servers use 4 CPU units and 8 GB memory.
Type B servers use 2 CPU units and 12 GB memory.
Total CPU usage is 20 units and memory usage is 72 GB.

## 4. Mathematical Operations
The equations are:
4x + 2y = 20
8x + 12y = 72

They are represented as Ax = b and solved using numpy.linalg.solve().

## 5. Implementation
NumPy stores the coefficient matrix and the right-hand-side vector. The solve() function calculates the unknown values.

## 6. Output Interpretation
The solution is 3 Type A servers and 4 Type B servers. The verification confirms that the calculated values reproduce the original CPU and memory totals.

## 7. Changing an Input Parameter
The total CPU usage is increased from 20 to 24 units while memory remains 72 GB. The number of servers calculated therefore changes.

## 8. Related Real-World Application
This method can help data-centre administrators estimate server combinations from available resource measurements.

## 9. Conclusion
Systems of linear equations provide a useful way of solving problems with multiple unknowns.
