n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('{} é maior que {}.'.format(n1,n2))
elif n1 < n2:
    print('{} é menor que {}.'.format(n1,n2))
else:
    print('{} e {} são iguais.'.format(n1,n2))
input('Pressione <ENTER> para encerrar.')