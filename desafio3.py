numero = 1000
soma = 0

while numero != 2001:
    if numero % 2 == 0:
        soma += numero
    numero += 1

print(f"A soma dos números pares entre 1000 e 2000 é {soma}")