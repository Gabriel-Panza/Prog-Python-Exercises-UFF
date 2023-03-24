codificated_word = input()
random_word = input()
word_decoded = []
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
for i in random_word:
    cont = 0
    for j in codificated_word:
        if i == j:
            word_decoded.append(alfabeto[cont])
        cont += 1
print("".join(word_decoded))