
# TASK 9: EIGENVALUES AND EIGENVECTORS

## Objective
To calculate eigenvalues and eigenvectors of a network adjacency matrix using NumPy.

## Input Values
A 4 by 4 adjacency matrix represents connections between four network nodes.

## Mathematical Operation
The relationship is Av = lambda*v, where lambda is an eigenvalue and v is an eigenvector.

## Implementation
NumPy's linalg.eig() calculates the eigenvalues and eigenvectors. The dominant eigenvector is normalized to estimate node importance.

## Output Interpretation
The dominant eigenvalue describes an important property of the network structure. The normalized scores estimate the relative importance of each node.

## Parameter Modification
An additional connection is added between nodes A and D. This changes the network structure and may change the dominant eigenvalue and importance scores.

## Real-World Application
This method can help analyse influential nodes in communication networks and social networks.

## Conclusion
Eigenvalues and eigenvectors help describe the structure and behaviour of connected systems.
