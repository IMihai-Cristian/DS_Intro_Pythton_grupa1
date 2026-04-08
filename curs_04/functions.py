""" Definitia unei functii """

# def nume_functie(parametru/parametrii):
#     print('am intrat in functie')
#     # set de instructii

# var = ''

def my_function():
    var = 'Rezultat'
    # print(var)
    return var

# print(var)
func = my_function()
# print(func)


""" namespace """ # asignarea este valabila doar in interiorul functiei

""" parametrii """

def func(nume, cantitate, device):
    result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
    return result

# info = func('Mihai', 20, 'calulatoare')
# print(info)
# info2 = func('Ana', 10, 'telefoane')
# print(info2)

"""argumente keyword """

# la keyword nu conteaza ordinea
# print(func(device='telefoane', cantitate=10, nume='Ana'))

# MIX (primele sunt argumentele pozitionale, urmate de cele cu keyword)
# print(func('Ana', device='telefoane', cantitate=10)) # aici e bine
# print(func(device='telefoane', cantitate=10, 'Ana')) # aici NU e bine


""" parametrii de tip default(standard) """

def func_2(nume='Radu', cantitate=100, device='ceasuri'):
    result = f'{nume} a comandat {cantitate} bucati din categoria {device}'
    return result

# print(func_2())
# print(func_2('Ion', 50))
# print(func_2(device='telefoane'))
# print(func_2('Andra', device='telefoane'))
# print(func_2('Andra', nume='Alina')) # daca pun pozitional, nu mai poate fi specificat keyword


"""rezumat:

CAZ 1: parametrii pozitionali: def func(a, b, c)
# 1. argumente pozitionale func(10, 20, 30) -> conteaza atat ordinea cat si ca nr. argumente = nr. parametrii
# 2. argumente keyword(c=10, a=20, b=30) -> nu conteaza ordinea ci doar nr. argumente = nr. parametrii
# 3. argumente mix(10, c=20, b=30) -> conteaza ca intotdeauna pozitional inainte si keyword dupa iar nr. argumente = nr. parametrii



# CAZ 2: parametrii default: def func(a=1, b=3, c=7)
# 1. argumente pozitionale func(10, 20, 30) -> conteaza ordinea si ca nr. argumente <= nr. parametrii
#                                              (daca sunt mai putine argumente, dupa ultimul furnizat restul preiau
#                                              valoarea default a parametrilor iar daca sunt mai multi-->eroare)
# 2. argumente keyword(c=10, a=20, b=30) -> nu conteaza ordinea ci doar ca nr. argumente <= nr. parametrii
# #                                        (daca sunt mai putine argumente, cele care lipsesc preiau
# #                                        valoarea default a parametrilor iar daca sunt mai multi-->eroare)
# 3. argumente mix(10, c=20, b=30) -> conteaza ca intotdeauna pozitional inainte si keyword dupa, iar nr. argumente <= nr. parametrii
# #                                        (daca sunt mai putine argumente, cele care lipsesc preiau
# #                                        valoarea default a parametrilor iar daca sunt mai multi-->eroare)


# CAZ 3: parametrii mix(pozitional cu default): def func(a, b=3, c=7)  
# se respecta ordinea cu param pozitionali primii
# unde am param pozitional se respecta regulile de la caz 1
# unde am param default se respecta regulile de la caz 2 """


""" return """

def calc(x):
    if x < 0:
        return  # daca nu am nimic scris in cod dupa return, functia returneaza None
    if x > 10:
        return
    # return
    # print(x)
    # a='aaa'

# res = calc(-2)
# print(res)
# res = calc(5)
# print(res)


""" Anotari """

def calc_2(a: int=0, b: int=1, c: int=2) -> int:
    """
    # Calculates the sum of three integers with default values provided.
    #
    # This function takes three integer parameters, computes their sum, and returns
    # the result. If no arguments are provided, the parameters default to the
    # values 0, 1, and 2 respectively.
    #
    # :param a: The first integer value. Defaults to 0.
    # :param b: The second integer value. Defaults to 1.
    # :param c: The third integer value. Defaults to 2.
    # :return: The sum of the input integers.
    # :rtype: int
    """
    return a + b + c


""" args si kwargs """

# def suma(a, b=0, *args): # args se noteaza dupa param pozitionali si cei default, cu * in fata
#     # print(type(args))
#     initial = a + b
#     total = 0
#     for elem in args:
#         # print(elem)
#         total += elem
#     return initial + total
#
#
# var = suma(1, 2, 3, 4, 5, 6, 7)
# print(var)


def suma(a, b=0, *args, **kwargs): # kwargs se noteaza dupa param pozitionali, cei default si cei cu * in fata. Se noteaza cu **
    initial = a + b
    total = 0
    for elem in args:
        total += elem
    for key, value in kwargs.items():
        total += value
    return initial + total

# var = suma(1, 2, 3, 4, 5, 6, c=7, d=8, e=9)
# print(var)

# var = suma(1, 2, 3, c=7, d=8, e=9)
# print(var)

# var = suma(1, 2, c=7, d=8, e=9)
# print(var)

# var = suma(1, 2, 3, c=7, d=8, e=9, 4, 5, 6)
# print(var)

# var = suma(1, 2, 3, c=7, d=8, e=9, a=4, b=5)
# print(var)


""" RECURSIVITATE """

# def test_func(nr):
#     if nr > 100:
#         return 101
#     else:
#         print(f'Nr este acum {nr}')
#         return test_func(nr+10)
#
# val = test_func(3)
# print(val)

# 3
# 13
# ---
# 93
# 101

var_test = '100'
