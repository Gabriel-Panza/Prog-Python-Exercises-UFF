players, rounds = [int(x) for x in input().split()]
entry = list(map(int, input().split()))
points = [0] * players

for i in range(players):
    points[i] = sum(entry[i::players])
    
points = points[::-1]
winner = players - points.index(max(points))
print(winner)