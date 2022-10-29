soma = 0
for c in range(3,500,3):
    if c % 2 == 1:
        soma += c
print ('A soma dos ímpares múltiplos de 3, de 1 a 500 é: {}.'.format(soma))