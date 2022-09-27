"""

A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
Write a Python program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. 
This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.

"""
import math

numberOfitems = float(input(f"How many items are there? "))

itemsPerbox = float(input(f"How many items are there per box? "))


boxesNeeded = math.ceil(numberOfitems / itemsPerbox)

print(f'For {numberOfitems:.0f} items and {itemsPerbox:.0f} items per box, you will need {boxesNeeded} boxes')