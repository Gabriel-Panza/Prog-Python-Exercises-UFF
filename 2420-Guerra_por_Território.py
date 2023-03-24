N = int(input())
sections = list(map(int, input().split()))
add=0
adds=0
intervals=0
for i in range(N):
    add+=sections[i]
while adds<(add/2):
    adds+=sections[intervals]
    intervals+=1
print(intervals)