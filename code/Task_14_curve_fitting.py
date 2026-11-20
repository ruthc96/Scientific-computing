import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Experimental data: hours of study and exam scores
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
scores = np.array([42, 48, 55, 61, 68, 73, 79, 84], dtype=float)

# Linear model: score = gradient * hours + intercept
def model(x, a, b):
    return a * x + b

# Estimate the model parameters
parameters, _ = curve_fit(model, hours, scores)
a, b = parameters

predicted = model(hours, a, b)

print("Gradient:", a)
print("Intercept:", b)
print("Predicted score after 9 hours:", model(9, a, b))

# Change one input: add 1 hour to the study time
print("Predicted score after 10 hours:", model(10, a, b))

# Plot the data and fitted line
x_line = np.linspace(1, 10, 100)
plt.scatter(hours, scores, label="Observed scores")
plt.plot(x_line, model(x_line, a, b), label="Fitted line")
plt.xlabel("Hours studied")
plt.ylabel("Exam score")
plt.title("Study Hours and Exam Scores")
plt.legend()
plt.grid(True)
plt.savefig("task14_curve_fitting.png")
plt.show()
