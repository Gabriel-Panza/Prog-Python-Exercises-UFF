coded_message=input()
code=input()
code_tries=0

for i in range(len(coded_message)-len(code)+1):
    pos=0
    verify=0
    for j in range(i, i+len(code)):
        if coded_message[j]==code[pos]:
            verify+=1
            break
        pos+=1
    if verify==0:
        code_tries+=1
print(code_tries)