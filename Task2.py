# Task 2: Using the Math Module for Calculations

import math
num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num)   # log base e
sine_value = math.sin(num)    # num is in radians

print(f"Square root of {num} is: {square_root}")
print(f"Natural logarithm of {num} is: {natural_log}")
print(f"Sine of {num} (in radians) is: {sine_value}")
