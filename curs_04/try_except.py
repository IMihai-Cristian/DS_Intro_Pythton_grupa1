""" TRY - EXCEPT"""

# var = 10
# print(var/0)

""" Raise Exception """

# var = 10
# if var > 5:
#     raise Exception('Aici este o eroare')

""" Blocul try/except """

# my_text = input('Introduceti un numar: ')
#
# # value = int(my_text)
# # print(value)
# # print(var_name)
#
# try:
#     value = int(my_text)
#     print(value)
#     print(var_name)
# except ValueError:
#     print('nu pot converti acest sir de caractere la int ')
# except NameError:
#     var_name = 100
#     print(f'nu cunosc ce valoare ai vrut sa printez asa ca am alocat valoarea default {var_name} ')
# except Exception as e:
#     print('intra pe exceptie: ', e)


""" else si finally """


my_text = input('Introduceti un numar: ')

# value = int(my_text)
# print(value)
# print(var_name)

try:
    value = int(my_text)
    print(value)
    print(var_name)
except ValueError:
    print('nu pot converti acest sir de caractere la int ')
except NameError:
    var_name = 100
    print(f'nu cunosc ce valoare ai vrut sa printez asa ca am alocat valoarea default {var_name} ')
except Exception as e:
    print('intra pe exceptie: ', e)
else:
    print('nu sunt exceptii')
finally:
    print('Print aici mereu')
