nome = input('Digite seu nome: ') # solicita ao usuário o nome
QTD_STR = len(nome)               # constante que usa a função (len) para ver a quantidade de strings tem na variável (nome)

try:
   if QTD_STR <= 3:
      print('Seu nome é curto.')
   elif QTD_STR >= 4 and QTD_STR <= 5:
      print('Seu nome é normal.')
   else:
      print('Seu nome é  muito grande.')
except:
   print('Digite mais de uma letra.')
