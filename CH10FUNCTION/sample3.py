import math
# Volume of a cylinder = PI x (radius ** 2) * height
def get_volume_of_a_cylinder(radius, height):
    volume = math.pi * (radius ** 2) * height
    print(f"The volume of the cylinder is {volume} cubic units")
get_volume_of_a_cylinder(21, 12)