# Jogo de adivinhar número
import random
from math import trunc

print('-='* 40)
print('Vou pensar em um número entre 0 e 100. Tente adivinhar...')

aleatorio = trunc(random.random()*101)

#Linha de comando  para verificar funcionalidade
#print(aleatorio)

numero = int(input('Qual número estou pensando: '))


if numero == aleatorio:
    print('Parabéns, você acertou!! Eu estava pensando em {}.'.format(aleatorio))
else:
    print('Que pena tente novamente, estava pensando em {}'.format(aleatorio))