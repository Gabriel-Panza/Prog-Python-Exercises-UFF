N_elem = int(input())
elem_sequencial = list(map(int, input().split()))
blocks = []
list_of_blocks = []
reason = elem_sequencial[1] - elem_sequencial[0]
blocks.append(elem_sequencial[0])
for i in range (1,N_elem-1):
    if (elem_sequencial[i] - elem_sequencial[i-1]) == reason:
        blocks.append(elem_sequencial[i])
    else:
        reason = elem_sequencial[i+1] - elem_sequencial[i]
        list_of_blocks.append(blocks)
        blocks.clear()
        blocks.append(elem_sequencial[i])
list_of_blocks.append(blocks)
if (elem_sequencial[N_elem-1] - elem_sequencial[N_elem-2]) == reason:
    blocks.append(elem_sequencial[N_elem-1])
else:
    list_of_blocks.append(blocks)
    blocks.clear()
    blocks.append(elem_sequencial[N_elem-1])
print(len(list_of_blocks))