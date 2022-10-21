from random import randint
from time import sleep

print('{:=^80}'.format(' Pedra, Papel ou Tesoura '))
print('Você jogará contra nosso COMPUTADOR, será que você tem a sorte ao seu lado para ganhar dele?')
print('')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma opção entre Pedra, Papel ou Tesoura:'
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA \n'
          'Jogue novamente')

else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    print('Você jogou {}'.format(itens[jogador]))
    sleep(1)
    print('O COMPUTADOR jogou {}'.format(itens[computador]))
    sleep(1)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU!!!')
    elif jogador == 2:
        print('COMPUTADOR VENCE')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU!!!')

elif computador == 2:
    if jogador == 0:
        print('VOCÊ VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
