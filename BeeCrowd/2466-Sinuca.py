initial_qnt_balls = int(input())
ball_lines = list(map(int, input().split()))

while initial_qnt_balls > 1:
    next_line_balls = []
    for i in range(initial_qnt_balls - 1):
        if ball_lines[i] == ball_lines[i+1]:
            next_line_balls.append(1)
        else:
            next_line_balls.append(-1)
    ball_lines = next_line_balls
    initial_qnt_balls -= 1

if ball_lines[0] == 1:
    print("black")
elif ball_lines[0] == -1:
    print("white")