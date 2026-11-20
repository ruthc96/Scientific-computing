
import numpy as np

# Network connections between four nodes
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

values, vectors = np.linalg.eig(A)

index = np.argmax(np.real(values))
dominant_value = np.real(values[index])
dominant_vector = np.abs(np.real(vectors[:, index]))

importance = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]

print("Dominant eigenvalue:", dominant_value)
print("Node importance:")

for node, score in zip(nodes, importance):
    print(node, round(score, 4))

# Change a network connection
A_modified = A.copy()
A_modified[0, 3] = 1
A_modified[3, 0] = 1

new_values, new_vectors = np.linalg.eig(A_modified)
print("Modified dominant eigenvalue:",
      max(np.real(new_values)))
