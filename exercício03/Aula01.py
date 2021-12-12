def f(var):
    print(var)


def dumb():
    return f

var = dumb()

print(id(var), id(f))

if var == f:
    var('var equal to f ')
else:
    print('not equal to f')

var('var can print something on the screen' )
var(type(var))

