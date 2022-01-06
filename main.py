# An exercise I took from my own head: eliminate repeated letters from words.
# Um exercício que eu tirei da minha cabeça: elimine letras repetidas de palavras.

word1 = "aaabbbcdecdecdefffg"
word2 = ""

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
while word2 < word1:

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

# If the letter is different, do a for loop passing through each letter of word2.
# Se a letra for diferente, fazer um for loop passando por cada letra da word2.
    else:
        for i_index, i_letter in enumerate(word2):

# If during the loop any matching letter is found inside word2...
# ...do a new loop in word2 starting at the repeated letter.
# Se durante o loop for encontrada alguma letra igual dentro de word2...
# ...fazer um novo loop em word2 a partir da letra repetida.
            if i_letter == word1[counter]:
                equal_letter_inside_word2 = True
                for j_index, j_letter in enumerate(word2[i_index:], start=i_index):

# During the new loop in word2, assess whether there is the same letter in word1 (starting at the current letter).
# If there is, add the letter index of word1 to list_index.
# Durante o novo loop em word2, avaliar se há letra igual em word1 (a partir da letra da vez).
# If there is, add the index of the letter present in word1 to list_index.
                    if j_letter == word1[counter + equal_letters]:
                        list_index.append(counter + equal_letters)
                        equal_letters += 1

# If any of the letters in word1 are different, continue the initial loop through word2.
# Se qualquer das letras em word1 for diferente, continuar o loop inicial através de word2.
# E se for a última letra de word2, quebrar o loop.
                    else:
                        equal_letters = 0
                        equal_letter_inside_word2 = False
                        list_index = []
                        if j_letter == word2[len(word2)-i_index]:
                            continue
                        else:
                            break

# If the number of letters in list_index is equal to the number of analyzed letters...
# ...then eliminate the letters of list_index from within word1.
# Se o número de letras em list_index for igual ao número de letra analisadas...
# ...então eliminar as letras de list_index de dentro de word1.
                if len(list_index) == (len(word2) - i_index):
                    word1 = word1[:list_index[0]] + word1[(list_index[0] + equal_letters-1):]
                    break

# If the loop was broken, due to the absence of a sequence of letters in word2 equal to word2...
# ...add in word2 the current letter.
# Se o loop foi quebrado, por ausência de uma sequência de letras em word2 igual a word2...
# ...adicionar em word2 a letra da vez.
        if equal_letter_inside_word2 == False:
            word2 += word1[counter]
            counter += 1

# Ended initial loop by word2, set variables to initial values.
# Terminado o loop inicial por word2, ajustar variáveis para os valores iniciais.
    equal_letters = 0
    list_index = []
    equal_letter_inside_word2 = False

print(f"currected word: {word1}")


