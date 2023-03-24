N_pins, height_M = map(int, input().split())
movements = 0
pins_height = list(map(int, input().split()))

for i in range(len(pins_height)):
    while pins_height[i] != height_M:
        if pins_height[i] < height_M:
            pins_height[i] += 1
            pins_height[i + 1] += 1
            movements += 1

        elif pins_height[i] > height_M:
            pins_height[i] -= 1
            pins_height[i + 1] -= 1
            movements += 1

while pins_height[-1] != height_M:
    if pins_height[-1] < height_M:
        pins_height[-1] += 1
        movements += 1

    elif pins_height[-1] > height_M:
        pins_height[-1] -= 1
        movements += 1

print(movements)
