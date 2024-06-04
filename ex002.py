entrada = input('Digite a hora: ')  #  solicita ao usuário a hora

try:
    hora = int(entrada)
    if hora >= 0 and hora < 11:
        print(f'Bom dia, {hora} horas.')
    elif hora >= 12 and hora < 17:
        print(f'Boa tarde, {hora} horas.')
    elif hora >= 18 and hora < 23:
        print(f'Boa noite, {hora} horas.')
except:
    print('Não conheço essa hora.')