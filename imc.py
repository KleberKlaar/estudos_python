peso = float(input('Digite o seu peso (em kg): ')) #Neste ponto o usuário digitará seu peso em quilogramas e a variável 'peso' receberá o valor.
altura = float(input('Digite sua altura (em metros): ')) #Neste ponto o usuário digitará sua altura e a variável 'altura' receberá o valor.
imc = round(peso/altura**2, 2) #Aqui realizamos o cálculo do IMC e a variável imc receberá o valor. Utilizamos "round" para que tenhamos somente duas casas decimais.
imc = str(imc) #Convertemos a variável imc para "string", visando concatenar quando formos imprimir ao usuário.
print('Seu IMC é '+imc+'kg/m².') #Finalmente imprimimos o valor do IMC.
input('Pressione <ENTER> para encerrar. ') #O programa será encerrado.