""" Declaratia IF """

# if expresie:
    # instructiune sau set de instructiuni

#ex 1
# first_number = 10
# second_number = 20
#
# if first_number < second_number: # se executa aici ptr ca outputul declaratiei este True
#     print('se respecta prima conditie')
# if first_number > second_number:
#     print('se respecta a doua conditie')


#ex 2
first_number = 10
second_number = 20

list_ex = ["rosu", "galben", "albastru"]

# if "galben" in list_ex: # True
#     print("expresia este adevarata")  # 1
#     if first_number > second_number: # False
#         print('a intrat pe primul if din interior expresie')
#     print('mesaj 1') # 2
#     if first_number <= second_number: # True
#         print('a intrat pe al doilea if din expresie')  # 3
#         print('mesaj 2') # 4
#     print('mesaj 3')  # 5
# print('mesaj 4') # 6


""" conditiile de else si elif """

# if expresie:
    # instructiune
# else:
    # instructiune

 # ex:3

# var_nr = 50
#
# if var_nr >= 50:
#     print('nr. este cel putin mai mare sau egal cu 50')
#     # print(f'Acesta este numarul ales: {var_nr}')
# else:
#     print('nr. este mai mic decat 50')
# print(f'Acesta este numarul ales: {var_nr}')


# ex.4

# val_1 = 20
# expression = False
# if expression:
#     val_1 = 40
# print(val_1)

# expression = False
# if expression:
#     val_1 = 40
# else:
#     val_1 = 20
# print(val_1)


# ex.5

# nume = input('Ce nume cauti?: ')
# if nume == 'Vlad':
#     print('Vlad exista')
# elif nume == 'Radu':
#     print('Radu exista')
# elif nume == 'Ana':
#     print('Ana exista')
# else:
#     print('numele nu exista')


""" instructiunea PASS """

# nume = input('Ce nume cauti?: ')
# if nume == 'Vlad':
#     print('Vlad exista')
# elif nume == 'Radu':
#     print('Radu exista')
# elif nume == 'Ana':
#     pass
# else:
#     print('numele nu exista')


""" operator Ternar """

# instructiune 1 if expresie else instructiune 2

var = 'cuvant'
var_ex = 10 if 'uv' in var else 20 # operator ternar
print(var_ex)

# vine din scrierea clasica:
if 'uv' in var:
    var_ex =10
else:
    var_ex = 20

# sau si mai simplu:
var_ex = 20
if 'uv' in var:
    var_ex = 10

