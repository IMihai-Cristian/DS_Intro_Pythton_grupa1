""" Functia Lambda """

element = lambda x: x * 10 # unde x este argument si x * 10 este expresie

# print(element(10))

def element_1(y):
    return y * 10

element_2 = lambda x, y: x + y
# print(element_2(11, 31))

""" FILTER """ # intoarce un obiect al clasei filter (care este defapt un iterator) rezultat prin aplicarea unei functii
# pe fiecare element dintr-un obiect iterabil (liste, tupluri, str ....)

list_1 = [1, 3, 6, 5, 18, 8, 2, 7, 3, 4, 11]
# program care sa returneze o lista care sa contina toate numerele pare dintr-o lista data

# cu filter
list_filter = filter(lambda var: (var % 2 == 0), list_1)
# print(list_filter)
# print(type(list_filter))
# print(list(list_filter))

# cu for clasic
list_for = []
for var in list_1:
    if var % 2 == 0:
        list_for.append(var)
# print(list_for)


# ex cu def:
def filtrare(var):
    if var % 2 == 0:
        return True
    else:
        return False

# print(list(filter(filtrare, list_1)))

a = range(1, 100)
# print(type(a))


""" MAP """ # intoarce un obiect al clasei map (care este defapt un iterator) rezultat prin aplicarea unei functii
# pe fiecare element dintr-un obiect iterabil (liste, tupluri, str ....)
list_1 = [1, 3, 6, 5, 18, 8, 2, 7, 3, 4, 11]
list_map = list(map(lambda var: var * 10, list_1))
# print(list_map)


""" ZIP """  # preia parametrii iterabili (0 sau mai multi) si returneaza un obiect al clasei zip (care este defapt un iterator)
# sub forma de tupluri, formate din grupuri de elemente provenite din parametrii initiali
# Lungimea finala a obiectului iterabil este egala cu lungimea celei mai scurte structuri initiale

list_with_int = [1, 2, 3, 4, 5, 6]
list_with_strings = ['one', 'two', 'three', 'four', 'five', 'six']
result = list(zip(list_with_int, list_with_strings))
# print(result)
list_with_floats = (1.1, 2.2, 3.3, 4.4, 5.5, 6.6)
result_2 = list(zip(list_with_int, list_with_strings, list_with_floats))
# print(result_2)

""" UNZIP """
result_unzip = zip(list_with_int, list_with_strings, list_with_floats)
# print(list(result_unzip))
val_1, val_2, val_3 = zip(*list(result_unzip))
# print('val_1 = ', list(val_1))
# print('val_2 = ', list(val_2))
# print('val_3 = ', list(val_3))


""" COMPREHENSION LIST """

var = 'comprehension'

# print(list(var), 78)

# caz forloop
list_for_loop = []
for elem in var:
    list_for_loop.append(elem)
# print(list_for_loop, 84)

# caz cu lambda
list_lambda = list(map(lambda x: x, var))
# print(list_lambda, 88)

# caz cu comprehension
list_comp = [elem for elem in var]
# print(list_comp, 92)

number_list = []
for x in range(20):
    if x % 2 == 0:
        number_list.append(x)
# print(number_list, 98)

number_list_2 = [x for x in range(20) if x % 2 == 0]
# print(number_list_2, 101)
# lista_noua = [expresie(element) for element in iterabil if conditie]

number_list_3 = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
# print(number_list_3, 105)

number_list_4 = ["Par" if x % 2 == 0 else 'Impar' for x in range(20)]
# print(number_list_4, 108)

""" COMPREHENSION DICTIONARY """

square_dict = {}
for num in range(1, 11):
    square_dict[num] = num * num
# print(square_dict, 115)

square_comp = {num: num * num for num in range(1, 11)}
# print(square_comp, 118)

""" any si all """

a = [41, 45]
b = [20, 41]
c = [45, 41]

# print(any(i in a for i in b)) # any verifica daca cel putin un element din b se gaseste in a
# print(all(i in a for i in b)) # all verifica daca toate elementele din b se gasesc in a
# print(all(i in a for i in c)) # all verifica daca toate elementele din b se gasesc in a

""" eval """

# value = eval('2 + 2')
# print(value)

# value_2 = '{1: 2}'
# print(value_2, type(value_2))
# value_3 = eval('{1: 2}')
# print(value_3, type(value_3))