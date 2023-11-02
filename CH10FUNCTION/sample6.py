import math
# Volume of a cylinder = PI x (radius ** 2) * height


def get_volume_of_a_cylinder(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
print(f"The volume of the cylinder is {get_volume_of_a_cylinder(radius, height)}")