numero = input('Digite um número inteiro: ') # solicita ao usuário um número inteiro.
try: # try para tentar executar o código, se o usuário nao digitar nada o except entra em uso.
    numero = int(numero) # --> para transformar a variavel (nome) em int
    if numero % 2 == 0:
        print('o número é par')
    else:
        print('o número é ímpar')
except:
    print('você não digitou um número inteiro')
