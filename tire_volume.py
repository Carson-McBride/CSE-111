"""


v= pi * w^2 *a(w*a + 2540*d) / 10,000,000,000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.




"""

from math import pi


volume = 0 
width = float(input("\nEnter width of tire in mm: "))
aspectRatio = float(input("Enter aspect ratio of tire: "))
diameter = float(input("Enter diameter of wheel in inches: "))


volume = (pi * width ** 2 * aspectRatio * (width * aspectRatio + 2540 * diameter)) / 10000000000

print (f'The approximate volume is {volume:.2f} liters')