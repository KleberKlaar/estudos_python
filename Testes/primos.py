n = int(input('Digite um número, para saber se ele é primo ou composto: '))
d = 0
for c in range (2,n):
    if n % c == 0:
        d += 1
if d == 0 or n == 1 or n == 2:
    print('O número {} é primo!'.format(n))
elif d != 0:
    print('O número {} é composto!'.format(n))