"""Write a Python program to calculate surface volume and area of a
cylinder
"""

PI = 3.14
radius = float(input('Please Enter the Radius of a Cylinder: '))
height = float(input('Please Enter the Height of a Cylinder: '))

surface_area = 2 * PI * radius * (radius + height) #2πr² + 2πrh 

print(surface_area)
radius2 = radius *radius
volume =  PI *radius2 * height #πr²h
print(volume)