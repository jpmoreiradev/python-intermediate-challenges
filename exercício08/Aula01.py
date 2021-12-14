# def func(arg, arg2):
#     return arg * arg2
#
# var = func(2, 2)
# print(var)
############################################
# a = lambda x, y: x * y
#
# print(a(2, 2))
###########################################
# lista = [
#     ['P1', 200],
#     ['P2', 150],
#     ['P3', 100],
#     ['P4', 50],
#     ['P5', 100],
#     ['P6', 150]
# ]
#
# def fun(item):
#     return item[1]
#
# lista.sort(key=fun, reverse=True)
#
# print(lista)
###########################################
# lista = [
#     ['P1', 200],
#     ['P2', 150],
#     ['P3', 100],
#     ['P4', 50],
#     ['P5', 100],
#     ['P6', 150]
# ]
#
#
# lista.sort(key=lambda item: item[1], reverse=True)
#
# print(lista)
##########################################
lista = [
    ['P1', 200],
    ['P2', 150],
    ['P3', 100],
    ['P4', 50],
    ['P5', 100],
    ['P6', 150]
]

print(sorted(lista, key=lambda i: i[1]))

