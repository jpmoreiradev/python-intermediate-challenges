
# def ola_mundo():
#     return "Hello World!"
#
# def mester(funcao):
#     return funcao()
#
# execute = mester(ola_mundo())
#
# print(execute)

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'João')
executando2 = mestre(saudacao, 'Pedro', saudacao='eae ')

print(executando2)
print(executando)