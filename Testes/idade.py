from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM.'.format(idade))
elif idade > 9 and idade <=14:
     print('O atleta tem {} anos e está na categoria INFANTIL.'.format(idade))
elif idade > 14 and idade <=19:
    print('O atleta tem {} anos e está na categoria JÚNIOR.'.format(idade))
elif idade > 19 and idade <=25:
    print('O atleta tem {} anos e está na categoria SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER.'.format(idade))