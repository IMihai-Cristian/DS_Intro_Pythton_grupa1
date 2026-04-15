def suma_test(a, b=0, *args, **kwargs): # kwargs se noteaza dupa param pozitionali, cei default si cei cu * in fata. Se noteaza cu **
    initial = a + b
    total = 0
    for elem in args:
        total += elem
    for key, value in kwargs.items():
        total += value
    return initial + total

var_exemplu_pachete = 100