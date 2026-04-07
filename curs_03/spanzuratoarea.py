# cuvant = 'elefant'
        # 'e l e f a n t'
        # 'e _ e _ _ _ t'
# reguli:
# - daca litera de inceput si cea de sfarsit se mai regaseste in interiorul cuv, aceasta se va afisa
# - 7 incercari;

# transformam cuvantul pentru a fi gata de joc:
# word = 'elefant'
word = input('Introduceti cuvantul: ').lower()
# print(word)
start_letter = word[0]
end_letter = word[-1]
display_word = ''
for i in word:
    # print(i)
    if i != start_letter and i != end_letter:
        i = '_'
    display_word += i
attempts = 7
tried_letters = []
while attempts > 0:
    print(f'Cuvantul este {display_word}. Mai ai {attempts} incercari.')
    letter = input('Introduceti o litera: ').lower()
    if len(letter) != 1:
        print('Va rugam sa introduceti doar o singura litera odata!')
        continue
    elif not letter.isalpha():
        print('Va rugam sa introduceti doar litere!')
        continue
    if letter in word.lower():
        if letter in tried_letters:
            print('Ai mai incercat aceasta litera deja!')
        else:
            for index, character in enumerate(word.lower()):
                if character == letter:
                    if letter not in tried_letters:
                        tried_letters.append(letter)
                    display_word = display_word[:index] + letter + display_word[index + 1:]
    else:
        if letter not in tried_letters:
            tried_letters.append(letter)
            attempts -= 1
            print(f'Litera nu exista! Mai ai {attempts} incercari')
            if attempts == 0:
                print(f'Ai pierdut! Cuvantul cautat era {word}')
        else:
            print('Ai mai incercat aceasta litera deja!')
    if '_' not in display_word:
        print(f'Felicitari! Ati castigat! Cuvantul gasit este {word}')
        break


