n50 = n20 = n10 = n5 = n2 = n1 = 0
valor = int(input('Digite o valor a ser sacado: '))
if valor >= 50:
    n50 = int(valor/50)
    valor = valor % 50
if valor >= 20:
    n20 = int(valor/20)
    valor = valor % 20
if valor >= 10:
    n10 = int(valor/10)
    valor = valor % 10
if valor >= 5:
    n5 = int(valor/5)
    valor = valor % 5
if valor >= 2:
    n2 = int(valor/2)
    valor = valor % 2
n1 = valor
print(f'Serão sacadas:\n - {n50} notas de R$50,00.\n - {n20} notas de R$20,00.\n - {n10} notas de R$10,00.\n - {n5} notas de R$5,00.\n - {n2} notas de R$2,00.\n - {n1} notas de R$1,00.\n')