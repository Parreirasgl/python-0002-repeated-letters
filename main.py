# Exercise I took from my own head: eliminate repeated letters from words.
# Exercício que eu tirei da minha cabeça: elimine letras repetidas de palavras.

word1 = "akaekarkart"
word2 = ""

length = len(word1)
counter = 0
while counter < length:
    print(counter)
    print(word1)

    if counter == 0:
        word2 += word1[0]
    elif word1[counter] == word2[len(word2)-1]:
        word1 = word1[:counter] + word1[(counter + 1):]
        counter -= 1
        length -= 1
    else:
        for i_index, i_letter in enumerate(word2):
            if i_letter == word1[counter]:
                for j_index, j_letter in enumerate(word2, start=i_index):
                    counter2 = 0
                    list_index = []
                    if j_letter == word1[counter + counter2]:
                        list_index = counter + counter2
                        counter2 += 1
                        if counter2 == (len(word2) - i_index):
                            for k in list_index:
                                word1 = word1[:k] + word1[(k + 1):]
                    else:
                        word2 += word1[counter]
                        break
    counter += 1

print(word1)
print(word2)


