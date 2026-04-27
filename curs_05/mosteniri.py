from abc import ABC


# class Example:
#
#     def __init__(self, val=1):
#         self.first = val
#
#     def set_second(self, valoare):
#         self.set_second = valoare
#         return self.set_second
#
# obj_1 = Example()
# # print(obj_1)
# print(obj_1.set_second(4))
# print(obj_1.__dict__)


# ------------------------------------

# class Example:
#
#     def __init__(self, val=1):
#         self.first = val
#
#     def set_second(self, valoare):
#         self.set_second = valoare
#         return self.set_second
#
# obj_1 = Example()
# # print(obj_1)
# print(obj_1.set_second(4))
# print(obj_1.__dict__) #{'first': 1, 'set_second': 4}
#
# obj_2 = Example(2)
# # print(obj_2.__dict__)
#
# obj_2.third = 5
# # print(obj_2.__dict__)


# ------------------------------------

# class Example:
#
#     def __init__(self, val=1):
#         self.__first = val
#
#     def set_second_method(self, valoare):
#         self.set_second = valoare
#         return self.set_second
#
# obj_1 = Example()
# # print(obj_1)
# # print(obj_1.first, 'linia 53')
# print(obj_1.set_second_method(4))
# print(obj_1.__dict__) # {'_Example__first': 1, 'set_second': 4}
# # print(obj_1._Example__first)
# print(obj_1.__dir__())


# ------------------------------------

# class Example:
#
#     counter = 0 # porprietate privata a clasei
#
#     def __init__(self, val=1):
#        self.__first = val
#        print(Example.counter)
#
# obj_1 = Example()
# # print(obj_1)


# -----------------------------------------

# class Vehicule:
#     pass
#
#
# class Masini(Vehicule):
#     pass
#
#
# class MasiniDeTeren(Masini):
#     pass
#
# print(issubclass(MasiniDeTeren, Vehicule))
# print(issubclass(Vehicule, MasiniDeTeren))


# -----------------------------------------

# class Vehicule:
#     pass
#
#
# class Masini(Vehicule):
#     pass
#
#
# class MasiniDeTeren(Masini):
#     pass
#
# vehicul_1 = Vehicule()
# masini_1 = Masini()
# masini_de_teren_1 = MasiniDeTeren()
#
# print(isinstance(masini_1, MasiniDeTeren))
# print(isinstance(masini_1, Masini))


# -----------------------------------------

# class SuperClasa:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
#
# class SubClasa(SuperClasa):
#     pass
#     # def __init__(self):
#     #     pass
#
#     def __str__(self):
#         return  f'Print {self.name}'
#
# # object_1 = SuperClasa('Mihai')
# # print(object_1)
#
# object_1 = SubClasa('Mihai')
# print(object_1)

# -----------------------------------------


# class SuperClasa:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
#
# class SubClasa(SuperClasa):
#     # pass
#     def __init__(self, name):
#         # SuperClasa.__init__(self, name)
#         # super(SuperClasa, self).__init__()           # cand am mostenire multipla
#         super().__init__(name)                             # bun doar la o singura mostenire
#         self.test = 'nume'
#
#     def __str__(self):
#         return  f'Print {self.test} {self.name}'
#
# # object_1 = SuperClasa('Mihai')
# # print(object_1)
#
# object_1 = SubClasa('Mihai')
# print(object_1)


# -----------------------------------------

# class SuperClasa:
#
#     def __init__(self, name='Mihai'):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
#
# class SubClasa(SuperClasa):
#
#     def __init__(self, aaa='Cristian'):
#         super().__init__(aaa)
#
#     def __str__(self):
#         return  f'Print {self.name}'
#
# object_1 = SubClasa('Ionel')
# print(object_1)


# --------


# class SuperClasa:
#
#     super_variabila = 'super'
#     sub_variabila = 'sub_parinte'
#
#     def __init__(self, name='Mihai'):
#         self.name = name
#
#     def __str__(self):
#         return f'Numele meu este {self.name}'
#
#
# class SubClasa(SuperClasa):
#
#     sub_variabila = 'sub'
#     super_variabila = 'super_copil'
#
#     def __init__(self, aaa='Cristian'):
#         super().__init__(aaa)
#
#     def __str__(self):
#         return f'Print {self.name}'
#
#
# obj_1 = SubClasa()
# print(obj_1.sub_variabila)
# print(obj_1.super_variabila)


# ---------------------------------------------------------------------


class SuperClasa:

    super_variabila = 'super'
    sub_variabila = 'sub_parinte'

    def __init__(self, name='Mihai'):
        self.name = name

    def __str__(self):
        return f'Numele meu este {self.name}'


class Mijloc:

    variabila_mijloc = 10
    super_variabila = 'mijloc'


class SubClasa(SuperClasa, Mijloc): # aici am mostenire multipla

    sub_variabila = 'sub'
    super_variabila = 'super_copil'

    def __init__(self, aaa='Cristian'):
        super().__init__(aaa)

    def __str__(self):
        return f'Print {self.name}'


obj_1 = SubClasa()
print(obj_1.super_variabila)
print(obj_1.variabila_mijloc)