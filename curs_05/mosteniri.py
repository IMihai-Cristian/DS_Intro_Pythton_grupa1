
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

class SuperClasa:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Numele meu este {self.name}'


class SubClasa(SuperClasa):
    pass
    # def __init__(self):
    #     pass

# object_1 = SuperClasa('Mihai')
# print(object_1)

object_1 = SubClasa('Mihai')
print(object_1)