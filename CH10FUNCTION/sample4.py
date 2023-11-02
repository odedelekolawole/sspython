import math
# Volume of a cylinder = PI x (radius ** 2) * height
def get_volume_of_a_cylinder(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume
print(get_volume_of_a_cylinder(21, 2))