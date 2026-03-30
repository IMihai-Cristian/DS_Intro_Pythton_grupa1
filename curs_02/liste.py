import math
""" listele sunt colectii de obiecte si sunt mutabile si ordonate (deci indexabile). Permit elemente duplicate"""

# var_list = []
# var_list_b = list()

# ex = 'programare'
# print(list(ex))

""" ordonare """
# list_1 = [1, 2, 3, 4]
# list_2 = [2, 1, 3, 4]


""" pot contine mai multe tipuri de elemente """
# list_var = [1, 2.5, 'Ana', '22', False, None]
# print(list_var)
# list_var_2 = [len, int, str, math]
# print(list_var_2)

""" concatenare -> extend """
# print([1, 2] + [3, 4] + [5, 6])

""" mutiplicare """
# result = list_1 * 3
# print(result)

""" lungimea len() """
# print(len(result))

""" indexare """
# list_idx = [1, 2.5, 'Ana', '22', False, None]
# print(list_idx[-1])

""" slicing """
# print(list_idx[::-1])

""" copierea unei liste """

# list_3 = [1, 2.5, 'Ana', '22', False, None]
# list_copy = list_3[:] # nu e acelasi obiect pentru ca liste sunt mutabile
# list_copy_1 = list_3
# print(list_copy is list_3)
# print(list_copy_1 is list_3)
# list_test = list_3.copy()
# print(list_test is list_3)

# # a = 1
# a = [1, 2.5, 'Ana', '22', False, None]
# # b = a
# # b = 1
# b = [1, 2.5, 'Ana', '22', False, None]

""" declarare multipla """

# list_names = ['Mihai', 'Andrei', 'George']
# [name_1, name_2, name_3] = list_names
# print(name_2)
# list_names_2 = ['Mihai', 'Andrei', 'George', 'Alina', 'Irina']
# (name_a, *name_b, name_c) = list_names_2
# print(name_a)
# print(name_b)
# print(name_c)


""" operatori in si not in """
# list_4 = [1, 2.5, 'Ana', '22', False, None]
# print('An' in list_4[2])


""" liste intretesute (nested) """
# list_5 = ['a', [3, ['22', 16, None], ['mere', False]], [3.55], 0]
# print(list_5[2][0])
# print(list_5[1][1][2])

""" modificare unui element prin index """
# list_6 = [1, 2.5, 'Ana', '22', False, None]
# list_6[-2] = True
# print(list_6)

""" cateva metode la liste """
# count
# list_m0 = [1, 2, 3, 4, 1, 5, 7, 1]
# print(list_m0.count(1))

# min si max
# list_m1 = [45, 34.3, 2, 10*2, 88.55]
# print(max(list_m1))
# print(min(list_m1))

# list_m2 = ['ana', 'merge', 'la', 'scoala']
# print(max(list_m2))
# print(min(list_m2))

# list_m3 = [1, 'ana', 44.3, 'ooo']
# print(max(list_m3))


# stergere element
# list_m5 = ['ana', 'merge', 'la', 'scoala']
# del list_m5[-2]
# print(list_m5)
# del list_m5
# print(list_m5)


# modificare prin slice
list_m6 = ['ana', 'merge', 'la', 'scoala']
# list_m6[1:3] = ['scrie', 'si', 'citeste']
# print(list_m6)
list_m6[2:] = []
# print(list_m6)


# adaugare elemente in lista
    # cu append
# list_m7 = [1, 2.5, 'Ana', '22', False, None]
# list_m7.append('ok')
# print(list_m7)
    # cu concatenare
# list_m7 += 'ion'
# list_m7 += ['ion']
# print(list_m7)
    # extend
# list_m7.extend(['ok', 'ion'])
# print(list_m7)
    # insert
# list_m7.insert(1, 11.11)
# print(list_m7)

list_m7 = [1, 2.5, 'Ana', '22', False, None]
# remove
# list_m7.remove('22')
# print(list_m7)

# pop
print(list_m7.pop())
# print(list_m7.pop(1))

#clear
# print(list_m7.clear())

# reverse
list_m7.reverse()
# print(list_m7)

# sort
list_m8 = ['ana', 'merge', 'la', 'scoala']
list_m8.sort(reverse=True)
# print('list_m8'.__dir__())