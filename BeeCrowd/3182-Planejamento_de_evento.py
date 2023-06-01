rooms = []
room = False
participants, budget, hotel_qnt, weeks_qnt = map(int, input().split())

for i in range(hotel_qnt):
    pricePerPerson = int(input())
    intNBeds = list(map(int, input().split()))
    total_price = participants * pricePerPerson
    for k in intNBeds:
        if participants <= k and total_price <= budget:
            rooms.append(total_price)
            set(rooms)
            room = True
best_price = 500000
for g in rooms:
    if g < best_price:
        best_price = g
if room:
    print(best_price)
else:
    print("stay home")
