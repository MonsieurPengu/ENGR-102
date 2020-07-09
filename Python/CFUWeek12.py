# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Ian Wang
# Section 510
# 227004716

# This program takes in a point in polar coordinates and returns a point in Cartesian coordinates.
import math
polarR = float(input("Polar R Coordinate = "))  # This asks for the polar R coordinate which will later turn into X.
polarTheta = float(input("Polar Theta Coordinate = "))  # This asks for the polar Theta coordinate
# which will later turn into Y.
cartesianX = polarR*math.cos(polarTheta)  # This will turn the user input R and Theta into X via rcos(theta).
cartesianY = polarR*math.sin(polarTheta)  # This will turn the user input R and Theta into Y via rsin(theta).
print("Based on the Polar Coordinates (r, theta) you entered, your Cartesian Coordinates are:"  
      "", "(", cartesianX, ",", cartesianY, ")")
# This will print or output the user's cartesian coordinates based on the polar coordinates they inputted.
