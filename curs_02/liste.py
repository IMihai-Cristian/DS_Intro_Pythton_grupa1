import math
""" listele sunt colectii de obiecte si sunt mutabile si ordonate (deci indexabile). Permit elemente duplicate"""

var_list = []
var_list_b = list()

# ex = 'programare'
# print(list(ex))

""" ordonare """
list_1 = [1, 2, 3, 4]
list_2 = [2, 1, 3, 4]


""" pot contine mai multe tipuri de elemente """
list_var = [1, 2.5, 'Ana', '22', False, None]
# print(list_var)
list_var_2 = [len, int, str, math]
# print(list_var_2)

""" concatenare -> extend"""
# print([1, 2] + [3, 4] + [5, 6])

""" mutiplicare """
result = list_1 * 3
# print(result)

""" lungimea len() """
# print(len(result))

""" indexare """
# list_idx = [1, 2.5, 'Ana', '22', False, None]
# print(list_idx[-1])

""" slicing """
# print(list_idx[::-1])

""" copiere unei liste """

list_3 = [1, 2.5, 'Ana', '22', False, None]
list_copy = list_3[:] # nu e acelasi obiect pentru ca liste sunt mutabile
list_copy_1 = list_3
# print(list_copy is list_3)
# print(list_copy_1 is list_3)
list_test = list_3.copy()
# print(list_test is list_3)

# # a = 1
# a = [1, 2.5, 'Ana', '22', False, None]
# # b = a
# # b = 1
# b = [1, 2.5, 'Ana', '22', False, None]

""" declare multipla """

# list_names = ['Mihai', 'Andrei', 'George']
# [name_1, name_2, name_3] = list_names
# print(name_2)
list_names_2 = ['Mihai', 'Andrei', 'George', 'Alina', 'Irina']
(name_a, *name_b, name_c) = list_names_2
print(name_a)
print(name_b)
print(name_c)