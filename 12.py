import math

print("Введите количество координат точек, которое будет введено: ", end="")
n = int(input())

print("Введите координаты точек, разделяя пробелами: ", end="\n")
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

def distance(point):
    x, y = point
    return math.sqrt(x*x + y*y)

points_sorted = sorted(points, key=lambda p: (distance(p), p[0], p[1]))

print("Координаты точек в порядке возрастания:")
for p in points_sorted:
    print(p[0], p[1])
