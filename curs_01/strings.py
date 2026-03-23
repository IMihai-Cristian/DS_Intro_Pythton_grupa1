""" siruri de caractere imutabile, indexabile """

# var = ''
# var1 = ""
# print(var, type(var))

""" concatenare """

# print('pro' + 'gram' + 'are')

# var1 = 'pro'
# var2 = 'gram'
# var3 = 'are'

# print(var1 + var2 + var3)

""" multiplicare """
# multip = 4
# print(multip * var1)
# var_test = -1 * var1
# print(id(var), id(var_test))

""" transformarea in string str() """
# print(43.5, type(43.5))
# print('43.5', type('43.5'))
# print(str(43.5), type(str(43.5)))

""" lungimea unui string len() """

# var = 'programare'
# print(len(var))

""" operatori in si not in """

# print('gr' in var)
# print('gr' not in var)

""" indexare """

# var = 'programare'
# var[index] -> indexarea incepe cu 0
# print(var[0]) -> primul caracter
# print(var[-1]) -> ultimul caracter
# print(var[10])
# print(var[len(var) - 1]) -> ca sa aflu indexul final
# print(var[-2])
# print(var[-len(var)])

""" slicing [start:stop:step] """
# var = 'programare'
     # 0123456789
     #    ->                 -2 .... -1 ....0 ....1 ......2
# print(var[1:10]) # rogramare
# print(var[2:6:5])
# print(var[-5::2])


""" interopolarea variabilelor in stringuri """

# var_1 = 'Python'
# var_2 = 'Digital Stack'
# var_3 = 'Mihai'
#
# # var_nume = input('Numele dvs. este: ')
# # print('Grupa de ' + var_1 + ' de la ' + var_2 + ' sustinuta de ' + var_nume)
#
# # caz 1 cu concatenare
# print('Grupa de ' + var_1 + ' de la ' + var_2 + ' sustinuta de ' + var_3, 1)
#
# # caz 2 cu .format
#     # cu acolade goale
# print('Grupa de {} de la {} sustinuta de {}'.format(var_1, var_2, var_3), 2)
#     # cu index in acolade
# print('Grupa de {1} de la {0} sustinuta de {2}'.format(var_2, var_1, var_3), 3)
#     # cu denumirea variabilei in acolada
# print('Grupa de {str_1} de la {str_2} sustinuta de {str_3}'.format(str_1='Python', str_2='Digital Stack', str_3='Mihai'), 4)
#
# caz 3 cu f'string' -> Python 3.6
# print(f'Grupa de {var_1.upper()} de la {var_2} sustinuta de {var_3}', 5)
#
# # varianta Python 2.0
# print('Grupa de %s de la %s sustinuta de %s' % (var_1, var_2, var_3), 6)


""" cateva metode folosite ptr stringuri """

var = 'programare'
var_1 = 'PROGRAMARE'
# print(var.capitalize())
# print(var.upper())
# print(var_1.lower())
var_2 = 'Ana banana'
# print(var_2.count('na'))
var_3 = 'Metode folosite la stringuri'
# print(var_3.find('folosite')) # returneaza index la care gaseste substring
# print(var_3.find('zzzz')) # daca nu exista substring returneaza -1
# print(var_3.index('folosite')) # returneaza index la care gaseste substring
# print(var_3.index('zzzz')) # EROARE
var_4 = ['Ana', 'are', 'mere', '!']
# print(" ".join(var_4))
var_5a = 'Ana are mere !'
# print(var_5a.split(''))
# var_5b = 'Ana, are mere, are pere, si, are struguri!'
# print(var_5b.split(','))
var_6 = '     programare      '
# print(var_6.lstrip())
# print(var_6.rstrip())
# print(var_6.strip())
var_7 = 'Ana are mere'
# print(var_7.replace('mere', ''))

# Fata spunea: 'buna ziua!'. " TEST " !
# print("""Fata spunea: 'buna ziua!'. " TEST " !""")


# Ex 1.

text = 'Python'
# print(text[:3])
# print(text[-2:])
# print(text[::-1])

# Ex 2.
text_2 = 'ha'
n = 3
# print(text_2 * n)

# Ex 3.
a = 'Ana'
b = 'mere'
# print(a + ' ' + b)
# print(f'{a} {b}')


# Replace that text from `var_string` between start and end with the text from `patches`
var_string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
patches = [[4, 14, "Conquistador"], [25, 31, "King"], [42, 49, "Palace"]]

