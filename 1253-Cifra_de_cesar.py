qnt_of_words = int(input())

for i in range(qnt_of_words):
    word = input()
    advance_qnt = int(input())
    word_decodificated = ""
    for j in word:
        letter = ord(j)-advance_qnt
        if letter < 65:
            word_decodificated += chr(91-(65-letter))
        else:
            word_decodificated += chr(letter)
    print(word_decodificated)