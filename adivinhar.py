#Importar
from random import randint

#Título
print('ADIVINHE O NÚMERO\nCriado por: Kleber Klaar')
#Texto
print('\nDescubra o número secreto, entre 1 e 10.')

#Variáveis
p = 0
n = randint(1,10)
t = 0

while p != n:
    p = int(input('Palpite: '))
    if p > n:
        print('O número secreto é menor que {}.'.format(p))
    elif p < n:
        print('O número secreto é maior que {}.'.format(p))
    t += 1
print('Você acertou! O número secreto é {}. Você precisou de {} tentativas.'.format(p,t))