soma = 0
for c in range(0,6):
    v = int(input('Digite um número: '))
    if v % 2 == 0:
        soma += v
print('A soma dos números pares digitados é: {}.'.format(soma))