#Martha Moreno Gonzalez
#02/28/2025
#Problem 1: returns the area of a circle

import math 

radius = int(input("Give the radius of the circle you want to find the area for: ")) 

def areaOfCircle(r):
    area = math.pi * r ** 2
    return area

print("Area of the circle: ", areaOfCircle(radius))
