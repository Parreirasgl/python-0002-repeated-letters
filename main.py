# An exercise I took from my own head: eliminate repeated letters from words.
# Um exercício que eu tirei da minha cabeça: elimine letras repetidas de palavras.

word1 = "jkaeekarkartyyp"
word2 = ""

length = len(word1)
counter = 0
equal_letter_inside_word2 = False
equal_letters = 0
list_index = []

# Create a while loop that runs a number of times equal to the word length.
# The word length will change during the loop due to exclusion of letters from the word.
# Thus, there must be correction in the variable counter when letters are excluded.
# Criar um lopp do tipo while que rode um número de vezes igual ao tamanho da palavra.
# O tamanho da palavra vai mudar durante o while loop, pelo fato de se excluir
# letras da palavra.
# Desse modo, deve haver correção na variável counter quando letras são excluídas.
while counter < length:
    print(f"counter: {counter}")
    print(f"word1: {word1}")
    print(f"word2: {word2}")
    print("")

# Add the first letter of word1 to word2.
# Adicionar a primeira letra de word1 em word2.
    if counter == 0:
        word2 += word1[0]
        counter += 1

# Compare the current turn letter (of word1) to the last letter of word2.
# If the letter is the same, delete such letter in word1, and correct the counter and length variables.
# Comparar a letra da vez de word1 à última letra de word2.
# Se a letra for igual, apagar tal letra a word1, e corrigir as variáveis counter e length.
    elif word1[counter] == word2[len(word2)-1]:
        word1 = word1[:counter] + word1[(counter + 1):]
        length -= 1
        print("letra da vez de w1 igual última letra de w2")

# If the letter is different, do a for loop passing through each letter of word2.
# Se a letra for diferente, fazer um for loop passando por cada letra da word2.
    else:
        for i_index, i_letter in enumerate(word2):
            print(f"i_index: {i_index}")
            print(f"i_letter: {i_letter}")
# Se durante for encontrada alguma letra igual dentro de word2...
# ...fazer um loop em word2 a partir da letra repetida.
            if i_letter == word1[counter]:
                equal_letter_inside_word2 = True
                for j_index, j_letter in enumerate(word2[i_index:], start=i_index):
                    print(f"j_index: {j_index}")
                    print(f"j_letter: {j_letter}")

# Durante o loop em word2, avaliar se há letra igual em word1, a partir da letra da vez.
# Se houver, adicionar o index da letra em list_index.
                    if j_letter == word1[counter + equal_letters]:
                        list_index.append(counter + equal_letters)
                        equal_letters += 1
                        print(f"list_index: {list_index}")
                        print(f"equal_letters: {equal_letters}")
                        print("")

# Se qualquer das letras em word1 for diferente, continuar o loop inicial através de word2.
                    else:
                        print("tem w2 dif w1")
                        print("")
                        equal_letters = 0
                        equal_letter_inside_word2 = False
                        list_index = []
                        if j_letter == word2[len(word2)-i_index]:
                            continue
                        else:
                            break

# Se o número de letras em list_index for igual ao número de letra analisadas...
# ...então eliminar as letras de list_index de dentro de word1.
                if len(list_index) == (len(word2) - i_index):
                    counter3=0
                    for k in list_index:
                        print(word1[k-counter3])
                        word1 = word1[:(k-counter3)] + word1[(k + 1-counter3):]
                        counter3 += 1
                        length -= 1
                    counter3 = 0
                    equal_letters = 100000
                    break

        if equal_letters == 100000:
            print(word1)
            print(word2)
            print("saída1")

        if equal_letter_inside_word2 == False:
            word2 += word1[counter]
            counter += 1
            print("saída2")

    equal_letters = 0
    list_index = []
    equal_letter_inside_word2 = False
    print("saída3")



