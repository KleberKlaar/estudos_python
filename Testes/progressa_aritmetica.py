v = int(input('Digite o primeiro valor da Progressão Aritmética: '))
r = int(input('Digite a razão da Progressão Aritmética: '))
c = 1
mais = 'S'
print(v)
while c < 10:
    c += 1
    v += r
    print(v)
mais = str(input('Você quer ver mais termos? [S/N] ')).upper()
while mais == 'S':
    t = int(input('Quantos outros termos deseja ver? '))
    c = 0
    while c < t:
        c += 1
        v += r
        print(v)
    mais = str(input('Você quer ver mais termos? [S/N] ')).upper()