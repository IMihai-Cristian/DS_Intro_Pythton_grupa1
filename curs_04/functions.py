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

print(func_2())
print(func_2('Ion', 50))
print(func_2(device='telefoane'))
print(func_2('Andra', device='telefoane'))
# print(func_2('Andra', nume='Alina')) # daca pun pozitional, nu mai poate fi specificat keyword
