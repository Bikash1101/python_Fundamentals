import math

def circle_stats(radius):
    area = round(math.pi * radius ** 2 , 2)
    circumferrence = round(2 * math.pi * radius , 2)
    return area , circumferrence

print(circle_stats(8))