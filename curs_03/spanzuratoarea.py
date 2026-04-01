# cuvant = 'elefant'
        # 'e l e f a n t'
        # 'e _ e _ _ _ t'
# reguli:
# - daca litera de inceput si cea de sfarsit se mai regaseste in interiorul cuv, aceasta se va afisa
# - 7 incercari;

# transformam cuvantul pentru a fi gata de joc:
word = 'elefant'
print(word)
start_letter = word[0]
end_letter = word[-1]
display_word = ''
for i in word:
    # print(i)
    if i != start_letter and i != end_letter:
        i = '_'
    display_word += i
print(display_word)
