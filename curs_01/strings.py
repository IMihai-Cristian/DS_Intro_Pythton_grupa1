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
var = 'programare'
     # 0123456789
     #    ->                 -2 .... -1 ....0 ....1 ......2
# print(var[1:10]) # rogramare
# print(var[2:6:5])
print(var[-5::2])