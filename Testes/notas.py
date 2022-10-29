n1 = float(input('Digite a nota do primeiro semestre: '))
n2 = float(input('Digite a nota do segundo semestre: '))
m = round((n1+n2)/2,1)
if m>=7:
    print('O estudante passou de ano com média {}.'.format(m))
elif m>=4 and m<7:
    print('O estudante está de recuperação com média {}.'.format(m))
else:
    print('O estudante reprovou com média {}.'.format(m))