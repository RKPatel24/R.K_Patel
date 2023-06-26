"""Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers."""

from decimal import *
data = list(map(Decimal, '3.64 4.692 26.45 48.45 12.60 10.04 90.25'.split()))
print("Maximum: ", max(data))
print("Minimum: ", min(data))