nome = str(input('Digite seu nome: '))
valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos pretende pagar a casa?' ))
salario_disponivel = salario * 0.3
parcelas = float(valor / (anos * 12))
if salario_disponivel > parcelas:
    parcelas = str(round(parcelas))
    print(nome+', o empréstimo foi aceito! O valor das parcelas será de: R$'+parcelas)
else:
    print(nome+', o empréstimo foi recusado.')