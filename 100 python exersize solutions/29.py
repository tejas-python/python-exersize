# Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.
import math
def volume(h,r=10):
    left = (4*math.pi*pow(r,3))/3
    right = (math.pi*pow(h,2)*(3*r -h))/3
    return left -right
print(volume(2))
