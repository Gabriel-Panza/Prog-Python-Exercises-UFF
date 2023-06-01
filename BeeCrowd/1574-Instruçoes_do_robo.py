sequencial_qnt = int(input())
movements = []
robot_position = []
for i in range(sequencial_qnt):
    distance_advanced = 0
    n = int(input())
    for j in range(n):
        instruction = input()
        if instruction == "LEFT":
            movements.append(-1)
        elif instruction == "RIGHT":
            movements.append(1)
        else:
            for b in range(1, n):
                if instruction == "SAME AS {}".format(b):
                    movements.append(movements[b - 1])
    for k in movements:
        distance_advanced += k
    robot_position.append(distance_advanced)
    movements.clear()
for h in robot_position:
    print(h)