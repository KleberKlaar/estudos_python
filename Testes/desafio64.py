n = 0
s = 0
d = -1
while n != 999:
    s += n
    d += 1
    n = int(input('Digite um valor: '))
print('Foram digitados {} números, e a soma entre eles é: {}.'.format(d,s))