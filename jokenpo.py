#Inicializando o jogo
from os import system
from random import randint
import time

jogo = 1
while jogo == 1:
    print('JOKENPÔ\n\nCriado por: Kleber Klaar\n')
    print('Escolha sua jogada:\n')
    escolha = int(input('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\nEscolha: '))
    cpu = randint(1,3)
    if escolha == 1:
        texto = "PEDRA"
    elif escolha == 2:
        texto = "PAPEL"
    elif escolha == 3:
        texto = "TESOURA"
    else:
        print('Opção inexistente.')
        jogo = 0
    if cpu == 1:
        texto_cpu = "PEDRA"
    elif cpu == 2:
        texto_cpu = "PAPEL"
    elif cpu == 3:
        texto_cpu = "TESOURA"
    time.sleep(1)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    time.sleep(1)
    print('-='*25+'-')
    if escolha == cpu:
        print('Jogador usou {} x CPU usou {}. Empate!'.format(texto, texto_cpu))
        print('-='*25+'-')
        novo = str(input('Jogar novamente? [S/N] '))
        if novo == 'S' or novo == 's':
            system('cls')
        else:
            jogo = 0
    else:
        if escolha == 1 and cpu == 3:
            print('Jogador usou {} x CPU usou {}. Jogador venceu!'.format(texto, texto_cpu))
            print('-='*25+'-')
            novo = str(input('Jogar novamente? [S/N] '))
            if novo == 'S' or novo == 's':
                system('cls')
            else:
                jogo = 0
        elif escolha == 2 and cpu == 1:
            print('Jogador usou {} x CPU usou {}. Jogador venceu!'.format(texto, texto_cpu))
            print('-='*25+'-')
            novo = str(input('Jogar novamente? [S/N] '))
            if novo == 'S' or novo == 's':
                system('cls')
            else:
                jogo = 0
        elif escolha == 3 and cpu == 2:
            print('Jogador usou {} x CPU usou {}. Jogador venceu!'.format(texto, texto_cpu))
            print('-='*25+'-')
            novo = str(input('Jogar novamente? [S/N] '))
            if novo == 'S' or novo == 's':
                system('cls')
            else:
                jogo = 0
        elif escolha == 1 and cpu == 2:
            print('Jogador usou {} x CPU usou {}. CPU venceu!'.format(texto, texto_cpu))
            print('-='*25+'-')
            novo = str(input('Jogar novamente? [S/N] '))
            if novo == 'S' or novo == 's':
                system('cls')
            else:
                jogo = 0
        elif escolha == 2 and cpu == 3:
            print('Jogador usou {} x CPU usou {}. CPU venceu!'.format(texto, texto_cpu))
            print('-='*25+'-')
            novo = str(input('Jogar novamente? [S/N] '))
            if novo == 'S' or novo == 's':
                system('cls')
            else:
                jogo = 0
        elif escolha == 3 and cpu == 1:
            print('Jogador usou {} x CPU usou {}. CPU venceu!'.format(texto, texto_cpu))
            print('-='*25+'-')
            novo = str(input('Jogar novamente? [S/N] '))
            if novo == 'S' or novo == 's':
                system('cls')
            else:
                jogo = 0