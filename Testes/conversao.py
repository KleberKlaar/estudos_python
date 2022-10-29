#Título do programa.
from os import system

print('CALCULADORA PARA CONVERSÃO DE BASES NUMÉRICAS')
print('Criado por: Kleber Klaar.\n')

#Inicializando o programa
iniciando = 1

while iniciando == 1:
    #Variáveis e captura de valores.
    valor = int(input('Digite o valor a ser convertido: '))
    print('\nEscolha para qual base numérica deseja converter.')
    base = str(input('[B]inário | [O]ctal | [H]exadecimal: '))
    print('') #Pulando uma linha.

    #Respostas
    if base == 'B' or base == 'b':
        print('O valor {} convertido para BINÁRIO é igual a: {}'.format(valor,bin(valor)[2:]))
        novamente = str(input('Converter outro valor? [S/N] '))
        system('cls')
        if novamente == 'n' or novamente == 'N':
            iniciando = 0
    elif base == 'O' or base == 'o':
        print('O valor {} convertido para OCTAL é igual a: {}'.format(valor,oct(valor)[2:]))
        novamente = str(input('Converter outro valor? [S/N] '))
        system('cls')
        if novamente == 'n' or novamente == 'N':
            iniciando = 0
    elif base == 'H' or base == 'h':
        print('O valor {} convertido para HEXADECIMAL é igual a: {}'.format(valor,hex(valor)[2:]))
        novamente = str(input('Converter outro valor? [S/N] '))
        system('cls')
        if novamente == 'n' or novamente == 'N':
            iniciando = 0
    else:
        novamente = str(input('Opção inexistente. Converter outro valor? [S/N] '))
        system('cls')
        if novamente == 'n' or novamente == 'N':
            iniciando = 0
print('Programa encerrado.')