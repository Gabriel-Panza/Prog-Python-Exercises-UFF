participants, rounds = map(int, input().split())
cont=1 
while participants!=0 or rounds != 0:
    initial_line = list(map(int, input().split()))
    for i in range(rounds):
        round = list(map(int, input().split()))
        restParticipants = round[2:]
        while 0 in initial_line:
            initial_line.remove(0)
        for j in range(len(restParticipants)):
            if restParticipants[j] != round[1]:
                initial_line[j] = 0           
    winner = max(initial_line)
    print("Teste {}".format(cont))
    print(winner)
    print()
    cont+=1
    participants, rounds = map(int, input().split())