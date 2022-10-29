c = 1
ma = me = s = int(input('Digite um valor: '))
continuar = str(input('Gostaria de digitar outro valor? [S/N] ')).upper()
while continuar == 'S':
    n = int(input('Digite outro valor: '))
    s += n
    c += 1
    if n > ma:
        ma = n
    if n < me:
        me = n
    continuar = str(input('Gostaria de digitar outro valor? [S/N] ')).upper()
print('A média dos valores digitados é: {}.'.format(s/c))
print('O maior valor digitado foi {} e o menor foi {}.'.format(ma,me))