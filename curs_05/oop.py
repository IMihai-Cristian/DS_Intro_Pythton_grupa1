# Tom este o pisica mare care doarme toata ziua

# object_name = Tom 9 (nume obiect)
# class_name = Pisica (numele clasei)
# property = marime pisica (proprietate a clasei/atribut) (adverb/adjectiv)
# activity = doarme (actiunea pe care o face obiectul) (verb)


# O masina Dacia merge repede

# object_name = Dacia
# class_name = masina
# property = repede
# activity = merge


# Catelul Dino are blana maro si latra tare

# object_name = Dino
# class_name = catel
# property = blano maro
# activity = latra


# class Dog:
#     pass


class Dog:

    def __init__(self):
        pass

obj_1 = Dog()
# print(type(obj_1))


# class Stack:

    # def __init__(self):
        # self.stack_list = []
        # self.__stack_list = []
        # print(self.__stack_list)

# obj_stiva = Stack()
# print(obj_stiva.stack_list)
# print(obj_stiva.__stack_list)



# #--------------------
# class Stack:
#
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, val):
#         self.__stack_list.append(val)
#         print(self.__stack_list)
#
#     def pop(self):
#         valoare = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         print(self.__stack_list)
#         return valoare
#
# obj_stiva = Stack()
# obj_stiva.push(1)
# obj_stiva.push(2)
# obj_stiva.push(3)
#
# print(obj_stiva.pop())
# print(obj_stiva.pop())
# print(obj_stiva.pop())


# #--------------------
# class Stack:
#
#     def __init__(self, val1):
#         self.__stack_list = []
#         self.val1 = val1
#
#     def push(self, val):
#         self.__stack_list.append(val)
#         print(self.__stack_list)
#         print(self.val1)
#
#     def pop(self):
#         valoare = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         print(self.__stack_list)
#         return valoare
#
# obj_stiva = Stack(4)
# obj_stiva.push(1)


#--------------------
class Stack:

    def __init__(self, val1):
        self.__stack_list = []
        self.val1 = val1

    def push(self):
        self.__stack_list.append(self.val1)
        print(self.__stack_list)

    def pop(self):
        valoare = self.__stack_list[-1]
        del self.__stack_list[-1]
        print(self.__stack_list)
        return valoare

obj_stiva = Stack(1)
obj_stiva_2 = Stack(5)
obj_stiva_3 = Stack(10)

# print(obj_stiva, obj_stiva_2, obj_stiva_3)
obj_stiva.push()
obj_stiva_2.push()
obj_stiva_3.push()



