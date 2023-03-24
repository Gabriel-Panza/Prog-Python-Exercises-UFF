Mx, My, Rx, Ry = map(int, input().split())
coordinates_x = Rx - Mx
coordinates_y = Ry - My
intersections = abs(coordinates_x) + abs(coordinates_y)
print(intersections)