# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Ian Wang, Brock, Rehmaan, Connor
# Section 510
# 227004716

# As a team, we have gone through all required sections of the tutorial, and each team member understands the material.
import numpy as np
A = np.arange(12).reshape(3, 4)  # Arranges 1 to 12 in a 3x4
B = np.arange(8).reshape(4, 2)  # Arranges 1 to 8 in a 4x2
C = np.arange(6).reshape(2, 3)  # Arranges 1 to 6 in a 2x3
D = np.arange(3).reshape(3, 1)  # Arranges 1 to 3 in a 3x1
print("----------------------")  # Print statements for every matrices
print("Matrix A")
print(A)
print("----------------------")
print("Matrix B")
print(B)
print("----------------------")
print("Matrix C")
print(C)
print("----------------------")
print("Matrix D")
print(D)
print("----------------------")
print("Matrix E")
E = A @ B @ C  # Product of 3 matrices
print(E)
print("----------------------")
print("Linear System Ex=D for X")
X = D/E  # Solves for the linear system of E and D
print(X)
