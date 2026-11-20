
# TASK 3: MATHEMATICAL FUNCTIONS AND VECTORIZATION

## 1. Introduction
This task demonstrates mathematical functions and vectorization using Python and NumPy.

## 2. Objective
To process a large collection of network latency measurements and compare normal looping with NumPy vectorization.

## 3. Input Values
The program generates one million network latency readings ranging from 5 to 250 milliseconds using a random number generator.

## 4. Mathematical Operations
- Convert milliseconds to seconds by dividing by 1000.
- Square each converted latency value.
- Calculate average latency.
- Measure execution time for both methods.

## 5. Implementation
The program uses a Python loop to process the readings individually. It then uses NumPy vectorization to perform the same operations on the entire array.

## 6. Output Interpretation
The program displays the first five squared latency values, execution times and approximate speed-up. Execution times depend on the computer used.

## 7. Changing an Input Parameter
The busy network scenario multiplies all latency readings by 1.5. This increases the average latency by 50%, demonstrating how increased network load affects response time.

## 8. Related Real-World Application
The technique can be used in server monitoring systems to analyse response times during normal and busy network conditions. It helps administrators identify performance changes and possible network delays.

## 9. Conclusion
Vectorization makes it easier to process large numerical datasets. NumPy performs operations on entire arrays without requiring an explicit Python loop.
