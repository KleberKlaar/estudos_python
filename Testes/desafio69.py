ma = ho = mu = 0
while True:
    id = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F] ')).upper()
    if id > 18:
        ma += 1
    if sexo == 'M':
        ho += 1
    if sexo == "F" and id < 20:
        mu += 1
    cont = str(input('Deseja cadastrar mais alguém? [S/N] ')).upper()
    if cont != 'S':
        break
print (f'Das pessoas cadastradas, {ma} têm mais de 18 anos, {ho} são homens e {mu} são mulheres com menos de 20 anos.')