from datetime import datetime

from math import pi

current_date_and_time = datetime.now()

volume = 0 
width = float(input("\nEnter width of tire in mm: "))
aspectRatio = float(input("Enter aspect ratio of tire: "))
diameter = float(input("Enter diameter of wheel in inches: "))


volume = (pi * width ** 2 * aspectRatio * (width * aspectRatio + 2540 * diameter)) / 10000000000

###print (f'The approximate volume is {volume:.2f} liters')

with open("volumes.txt", mode="at") as volumes_file:
    print(f"date: {current_date_and_time:%m-%d-%Y}, width: {width}, aspect ratio: {aspectRatio},\
 diameter: {diameter}, volume: {volume:.2f}", sep=" ", end="\n", file=volumes_file)