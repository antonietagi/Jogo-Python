import random
#variável = random.choice('pedra', 'papel', 'tesoura')
print('Bem vindos ao clássico game PPeT!')
print('Para começar o jogo, terememos algumas regras, \nvocês tem que escolher uma das seguintes opções: Pedra, Papel e Tesoura.')
print()


print('\033[1;36m====PRIMEIRA JOGADORA====\033[m')
nome = input('Qual é o seu nome?')

nome2 = 'computador'

pontos1 = 0
pontos2 = 0

rodadas = 3
for i in range (1,4):
    jogadoraUm = input(f'\n{nome}, qual será a sua jogada?').lower()

    while jogadoraUm != 'pedra' and jogadoraUm != 'papel' and jogadoraUm != 'tesoura':
      print('INVÁLIDO, jogue novamente')
      jogadoraUm = input(f'\n{nome}, qual será a sua jogada?').lower()

      #print('===SEGUNDA JOGADORA====')
      jogadoraDo = random.choice(['pedra', 'papel', 'tesoura'])
      #jogadoraDo = input(f'{nome2}, qual será a sua jogada?').lower()
      #while jogadoraDo != 'pedra' and jogadoraDo != 'papel' and jogadoraDo != 'tesoura':
                                 #print('INVÁLIDO, jogue novamente')
                                 #ogadoraDo = input(f'{nome2}, qual será a sua jogada?').lower()


    print(f'\nA jogadora {nome} escolheu {jogadoraUm} e o {nome2} escolheu {jogadoraDo}.')

    if jogadoraUm == jogadoraDo:
          print(f'{nome} e {nome2} EMPATARAM a rodada {i}.')

    elif jogadoraUm == 'pedra' and jogadoraDo == 'tesoura':
          print(f'{nome} GANHOU a rodada {i}')
          pontos1 = pontos1 + 1

    elif jogadoraUm == 'papel' and jogadoraDo == 'pedra':
          print(f'{nome}GANHOU a rodada {i}')
          pontos1 = pontos1 + 1

    elif jogadoraUm == 'tesoura' and jogadoraDo == 'papel':
          print(f'{nome} GANHOU a rodada {i}')
          pontos1 = pontos1 + 1
    else:
          print(f'A jogadora {nome2} ganhou a rodada {i}')
          pontos2 = pontos2 + 1

if pontos1 > pontos2:
  print(f'\n{nome} é a VENCEDORA.')
elif pontos2 > pontos1:
  print(f'\n{nome2} VENCEU.')
else:
  print('\nAs duas EMPATARAM')



