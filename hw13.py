#Name: Ian Wang
#UIN: 227004716
#Engr 216 - 524

import matplotlib.pyplot as plt
import numpy as np

m = int(input("Your m value: "))
b = int(input("Your b value: "))
k = int(input("Your k value: "))
xo = int(input("Your x not value: "))

beta = b/(2*m)
omega = k/m

if (beta*beta) > (omega*omega):
    print("Your value for B is: ", beta)
    print("Your value for w is: ", omega)
    print("The system is overdamped.")
if (beta*beta) < (omega*omega):
    print("Your value for B is: ", beta)
    print("Your value for w is: ", omega)
    print("The system is underdamped")
if (beta*beta) == (omega*omega):
    print("Your value for B is: ", beta)
    print("Your value for w is: ", omega)
    print("The system is critically damped")

#Enter time values in integers starting with 1,2,3,4...n+1
#Enter 0 for stop
x = int(input("Time values for x-axis: "))
y = int(input("Re-enter your x not values: "))
while x > 0:
    x = int(input("Time values for x-axis: "))
    y = int(input("Re-enter your x not values: "))
    plt.plot()
plt.title('Dampening Plot')
plt.xlabel('Time')
plt.ylabel('User x not values')
plt.show()

#For some reason i couldn't get the plot to show, however I'll still snip it due to given instruction.