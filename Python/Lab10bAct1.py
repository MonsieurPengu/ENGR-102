# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Ian Wang
# Section 510
# 227004716
import numpy as np
import matplotlib.pyplot as plt
Count = 0
v = np.matrix('1; 0')
M = np.matrix('1.00583 -0.087156; 0.087156 1.00583')
while Count <= 150:
    vPrime = M @ v
    y = plt.plot(vPrime)
    Count += 1
plt.xlabel('v points')
plt.ylabel('M points')
plt.title('Matrices on a graph')
plt.show()
