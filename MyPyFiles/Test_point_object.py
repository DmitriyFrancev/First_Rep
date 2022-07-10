from Point import Point

point1 = Point(10, 15)
point2 = Point(15, 22)

print(point1.x, point1.y)
print(point2.x, point2.y)

print(point1.distance_to(point2))
print(point2.distance_to(point2))

print(point1)
print(type(point1))