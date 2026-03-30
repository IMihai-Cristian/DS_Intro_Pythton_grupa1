""" dictionarele sunt colectii de obiecte si sunt mutabile si ordonate (deci indexabile, incepand cu Python 3.7). Nu permit elemente duplicat """

# var_dict = {}
# var_dict_2 = dict()

"""cheile din dictionar"""
# var_dict = {'cheie_1': 'valoare_1', 'cheie_2': 'valoare_1'} -> cheile sunt unice intr-un dictionar si pot fi doar imutabile
# print(var_dict)
# var_dict = {[22.5, 12, 'aaaa']: 'valoare_1', 'cheie_2': 'valoare_1'}
# print(var_dict)

"""valorile din dictionar"""
# var_dict = {1: 'a', 'a': 1, 'list_1': [1, '2', 'trei', 4.4], 'dict': {'dict2': 100}}
# var_dict = {1: 'b', 'a': 'b', 'list_1': 'b', 'dict': 'b'}
# print(var_dict)

"""lungimea len()"""
# print(len(var_dict))


"""indexare"""
# print(var_dict['list_1'])


"""dictionar intretesut"""
var_dict = {
    1: 'a',
    'a': 1,
    'list_1': [1, '2', ('trei', {'aaa': [1, 'ccc']}), 4.4],
    'dict': {'dict2': 100},
    'dict_var': {'dict2': {100: 22.22}}
}
# print(var_dict['list_1'][2][1]['aaa'])
# print(var_dict['dict_var']['dict2'][100])


""" alocarea de elemente noi """

var_dict_2 = {'key_1': 1, 'key_2': 2}
# var_dict_2['key_3'] = 3 # daca cheia nu exista, se adauga cheie:valoare la sfarsit de dict
# print(var_dict_2)
# var_dict_2['key_2'] = 'doi' # daca cheia exista, se inlocuieste valoarea aferenta cheii
# print(var_dict_2)


""" metode folosite la dict """
# clear

# get
# print(var_dict_2['key_3'])
# print(var_dict_2.get('key_2', 'nu exista cheie'))

# items()
# print(var_dict_2.items())

# keys()
# print(var_dict_2.keys())

# values()
# print(var_dict_2.values())

var_dict_2 = {'key_1': 1, 'key_2': 2}
# pop() # sterge din dictionar si pastreaza in acelasi timp valoarea stearsa (cu mentiunea ca in metoda pop se specifica cheia)
# print(var_dict_2.pop('key_2'))

# popitem() # returneaza ultimul element de forma cheie-valoare. Nu trebuie specificata cheia, o ia mereu pe ultima gasita
# print(var_dict_2.popitem())

# update()
var_dict_2.update({'key_2': 3, 'key_4': 4})
print(var_dict_2)