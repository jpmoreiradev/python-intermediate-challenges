def saudacao(msg="Hollá", nome="JP"):
    nome = nome.replace("e", "3")
    msg = msg.replace("e", "3")
    return f'{msg} {nome}'

variavel = saudacao()


print(variavel)
print(variavel)
