nome = str(input('Qual é o seu nome? '))
if nome == 'Kleber':
    print('Que nome bonito!')
elif nome == 'José' or nome == 'Joaquim':
    print('Seu nome é de idoso.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))