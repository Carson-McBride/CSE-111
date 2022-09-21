"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""


age = float(input("How old are you? "))
heartRate = 220 - age

hr_Minimum = heartRate * 0.65
hr_Maximum = heartRate * 0.85

print (f"When you exercise to strengthen your heart, you should keep your heart rate between {hr_Minimum:.0f} and {hr_Maximum:.0f} ")

