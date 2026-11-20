
import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix operations
addition = A + B
multiplication = A @ B
determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

print("Matrix Addition:")
print(addition)

print("Matrix Multiplication:")
print(multiplication)

print("Determinant of A:", determinant)

print("Inverse of A:")
print(inverse)

# Change one input value
A_modified = np.array([[2, 2], [3, 4]])
print("Modified matrix multiplication:")
print(A_modified @ B)
