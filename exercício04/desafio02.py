# def aumento_porcentual(value, porcentual):
#     return value - (value * porcentual / 100)
#
# ap = aumento_porcentual(50, 10)
# print(ap)
# ap = aumento_porcentual(100, 10)
# print(ap)
# ap = aumento_porcentual(10, 10)
# print(ap)

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz'
    if n % 3 == 0:
        return f'fizz'
    if n % 5 == 0:
        return f'buzz'
    return n

from random import randint

for i in range(100):
    random = randint(0, 100)
    print(fb(random))
