""" seturile sunt colectii de obiecte si sunt mutabile si neordonate (deci neindexabile). Nu permit elemente duplicate"""

var_set = set()
# print({None, 'aaaa', None, 22.3, 55})
# var_set_ex = {}
# print(type(var_set_ex))
# print(set('Abc'))

""" pot contine mai multe tipuri de elemente (doar imutabile)"""
# set_1 = {None, 'aaaa', None, 22.3, 55, (1, 133, 'vasile')} # asa merge
# set_1 = {None, 'aaaa', None, 22.3, 55, [1, 133, 'vasile']} # asa nu merge
# print(set_1)

"""concatenare""" # nu merge concatenarea
# print({'a', 'b'} + {'c', 'd'})

""" dimensiunea unui set cu len() """
set_3 = {None, 'aaaa', None, 22.3, 55}
# print(len(set_3))

""" operatii in seturi """

# var_set_1 = {'a', 'b', 'c'}
# var_set_2 = {'a', 'e', 'f'}

"""UNION (preia toate elementele care nu sunt duplicat)"""
# varianta 1
# print(var_set_1.union(var_set_2))
# varianta 2
# print(var_set_1 | var_set_2)

var_3 = ('a', 'e', 'f')
# print(var_set_1.union(var_3))
# print(var_set_1 | var_3)

"""INTERSECTION (preia toate elementele comune)"""

# var_set_1 = {'a', 'b', 'c'}
# var_set_2 = {'a', 'e', 'f'}
# print(var_set_1.intersection(var_set_2))
# print(var_set_1 & var_set_2)

"""DIFFERENCE (lasa ce nu ramane comun din primul)"""
# print(var_set_1.difference(var_set_2))
# print(var_set_1 - var_set_2)

"""SYMMETRIC DIFFERENCE (preia din ambele seturi ce nu e comun)"""
# print(var_set_1.symmetric_difference(var_set_2))
# print(var_set_1 ^ var_set_2)

"""METODE LA SETURI """
# UPDATE -> adauga elementele altui iterabil la set
# var_set_1.update((1, ))
# print(var_set_1)

# ADD -> adauga un element la set
# var_set_1.add((1, 2))
# print(var_set_1)

var_set_1 = {'a', 'b', 'c'}
var_set_2 = {'a', 'e', 'f'}

# REMOVE
# var_set_1.remove('x') # sterge un element dar important este sa existe in set
# print(var_set_1)

# DISCARD
# var_set_1.discard('x') # sterge un element dar daca nu exista, lasa setul asa cum este
# print(var_set_1)

# POP
var_set_1.pop() # elimina un element la intamplare (nu stim care ptr ca setul este neordonabil)
# print(var_set_1)

# CLEAR
var_set_1.clear() # goleste tot setul
# print(var_set_1)

# var_string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# patches = [[4, 14, "Conquistador"], [25, 31, "King"], [42, 49, "Palace"]]
# print(var_string.replace(var_string[patches[0][0]:patches[0][1]], patches[0][2]).replace(var_string[patches[1][0]:patches[0][1]], patches[1][2]))