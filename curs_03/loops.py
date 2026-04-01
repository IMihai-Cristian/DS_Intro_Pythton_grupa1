""" FOR LOOP """ # for-ul este folosit pentru a parcurge un obiect iterabil; este o bucla finita

# for <variabila temporara> in <iterabil>:
    # instructiune

# ex.1

# list_ex = ['unu', 'doi', 'trei']
# print(var)
# for var in list_ex:
#     a = 10
    # print(var)

# print(var)

# var_dict = {'key_1': 1, 'key_2': 2, 'key_3': 3, 'key_4': 4}
# for x in var_dict:
#     print(x)
#
# for y in var_dict.keys():
#     print(y)

# for x in var_dict:
#     print(var_dict[x])
# print('-------------------------------')
# for y in var_dict.values():
#     print(y)

# for key, value in var_dict.items():
#     print(f'Cheia: {key} -> are valoarea {value}')

""" FOR cu enumerate """
# list_ex = ['unu', 'doi', 'trei']
# for index, elem in enumerate(list_ex, start=111):
#     print(index, '->', elem)


""" FOR cu RANGE """
# for item in range(10):
#     print(item)
# a = []
# for item in range(1, 10, 2):
#     a.append(item)
# print(a)

# a = []
# for item in range(-100, 101, 2):
#     a.append(item)
# print(a)

""" BREAK si CONTINUE """


# for animal in ['urs', 'velociraptor', 'maimuta', 'vulpe', 'melc', 'marmota']:
#     if animal.startswith('m'):
#         continue
#     print(animal)

# for animal in ['urs', 'velociraptor', 'maimuta', 'vulpe', 'melc', 'marmota']:
#     if animal.startswith('m'):
#         break
#     print(animal)

# for animal in ['urs', 'velociraptor', 'maimuta', 'vulpe', 'melc', 'marmota']:
#     if animal.startswith('m'):
#         pass
#     print(animal)


""" FOR poate avea si ELSE """
# for animal in ['urs', 'velociraptor', 'maimuta', 'vulpe', 'melc', 'marmota']:
#     print(animal)
# else:
#     print('OK')  # in situatia asta cand for se executa complet, interpretorul executa si ELSE

# for animal in ['urs', 'velociraptor', 'maimuta', 'vulpe', 'melc', 'marmota']:
#     print(animal)
#     break
# else:
#     print('OK') # in situatia asta cand for NU se executa complet, interpretorul NU executa ELSE




""" WHILE """ # este folosit pentru a repeta o instructiune sau un set de instrunctiuni, atata timp cat este validata conditia
# din definitia acestuia --> ATENTIE: instructiunea poate fi repetata la infinit

# while conditie: # daca este echivalata cu True atunci se executa
    # instructiune

# nr = 5
# while nr > 0:
#     print(nr)
#     nr -= 1

# nr = 0
# while nr > 0:
#     nr -= 1
#     print(nr)

# animal = ['urs', 'velociraptor', 'maimuta', 'vulpe', 'melc', 'marmota']
# while animal:
#     print(animal.pop(-1))
#     print(animal)


""" BREAK si CONTINUE """

# nr = 5
# while nr > 0:
#     nr -= 1
#     if nr == 1:
#         break
#     print(nr)
# print('Final')

# nr = 5
# while nr > 0:
#     nr -= 1
#     if nr == 1:
#         continue
#     print(nr)
# print('Final')


""" ELSE """

# nr = 5
# while nr > 0:
#     nr -= 1
#     if nr == 1:
#         break
#     print(nr)
# else:
#     print('Final')


# exercitiu

"""Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
afisati numarul pozitiv."""


# nr = input("Da-mi o valoare pentru nr.: ")
# if nr > 0:
#     if nr < 10:
#         print('Ai introdus nr. mai mic decat 10')
#     else:
#         pass
# if nr.isdigit():
#     if 0 < int(nr) < 10:
#         print('Ai introdus nr. mai mic decat 10')
#     elif int(nr) >= 10:
#         print('Ai introdus nr. mai mare sau egal decat 10')
#     elif nr == 0:
#         print('Numarul este 0')
#     else:
#         print(f'Numarul introdus este {nr} si modul lui este {abs(int(nr))}')
# else:
#     nr = input("Da-mi o valoare pentru nr.: ")

# START (input) -> FLUX LOGIC -> STOP (output)

# De pus si while


""" DECLARATIILE MATCH/CASE """

# ex:

car = 'BMW'

match car:
    case 'Audi' | 'BMW':
        print('German car')
    case 'Dacia':
        print('Romanian car')
    case 'Toyota':
        print('Japanese car')
    case _:
        print('Other cars')