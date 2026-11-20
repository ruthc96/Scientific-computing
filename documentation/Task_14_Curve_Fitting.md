# Task 14: Curve Fitting and Approximation

## Objective
To use curve fitting to estimate the relationship between study hours and exam scores.

## Input Data
The input consists of study hours:
1, 2, 3, 4, 5, 6, 7 and 8 hours.

The corresponding observed exam scores are:
42, 48, 55, 61, 68, 73, 79 and 84.

## Mathematical Operation
A linear model is used:

score = a × hours + b

The SciPy curve_fit function estimates the gradient (a) and intercept (b) that best fit the observations.

## Output and Interpretation
The program displays the estimated model parameters and predicts scores for 9 and 10 study hours.

The graph compares the observed scores with the fitted straight line. It helps show the general relationship between study time and performance.

## Changed Input
The prediction is changed from 9 study hours to 10 study hours. The predicted score increases because the fitted model shows a positive relationship between study hours and exam scores.

## Real-World Application
A school can use this approach to study how learning time relates to student performance.

Assumption: The relationship is approximately linear within the range being considered. The model is an estimate and does not prove that study time alone determines exam results.
