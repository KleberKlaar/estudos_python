media = 0
nome = ''
velho = 0
mulheres = 0

for c in range(1,5):
    nome2 = str(input('Digite o nome {}: '.format(c)))
    idade = int(input('Digite a idade {}: '.format(c)))
    sexo = str(input('Digite o sexo{} [M/F]: '.format(c)))
    media += idade/4
    if sexo == 'M' or sexo == 'm':
        if idade > velho:
            nome = nome2
    elif sexo == 'F' or sexo =='f':
        if idade < 21:
            mulheres += 1
print('A média de idade do grupo selecionado é: {}.'.format(media))
print('O homem mais velho do grupo é: {}.'.format(nome))
print('{} mulheres têm menos de 21 anos.'.format(mulheres))