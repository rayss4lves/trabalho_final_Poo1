def teste(nome = None, idade = None):
    if nome:
        nome = 'Anônimo'
    elif idade:
        idade = 0
nome = 'rayssa'
teste1 = teste(nome)

print(teste1)