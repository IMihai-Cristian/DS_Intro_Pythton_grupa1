""" module """
import os
import sys

# - import pentru a prelua functionalitati din alte scripturi

# from functions import suma, var_test
#
# print(suma(1, 2, 3, 4, var_1=5, alta_var=6), var_test)

""" alias as """

# from functions import suma as my_function_test, var_test as alta_variabila
# print(my_function_test(1, 2, 3, 4, var_1=5, alta_var=6), alta_variabila)

""" import direct """
import functions
# print(functions.suma(1, 2, 3, 4, var_1=5, alta_var=6))

""" __file__ """
# print(functions.__file__)

"""dir"""
# print(dir(functions.var_test))

import curs_02.fisier_import_pachete as pachet
# print(sys.path)
# print(pachet.suma_test(1, 2))

# /home/mihai/Digital Stack/DS_Intro_Pythton_gr1

# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

lista_pathuri = sys.path
cale_proiect_py = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


a = 'Exista' if '/home/mihai/Digital Stack/DS_Intro_Pythton_gr1' in sys.path else 'Nu exista'
print(a)
#
# for x, y in enumerate(sys.path):
#     print(x, y)
#     if y == '/home/mihai/Digital Stack/DS_Intro_Pythton_gr1':
#         sys.path.remove(y)

a = 'Exista' if '/home/mihai/Digital Stack/DS_Intro_Pythton_gr1' in sys.path else 'Nu exista'
print(a)

sys.path.remove('/home/mihai/Digital Stack/DS_Intro_Pythton_gr1')
print(sys.path)


import curs_02.fisier_import_pachete as pachet
print(pachet.suma_test(2, 3))
