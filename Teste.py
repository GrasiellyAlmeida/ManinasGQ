from random import shuffle
def cria_baralho():
    cartas = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♠', 'Q♠', 'K♠', 'J♥', 'Q♥', 'K♥', 'J♦', 'Q♦', 'K♦', 'J♣', 'Q♣', 'K♣']
    lista = shuffle(cartas)
    return cartas
 
def extrai_naipe(carta):
    if carta == '10♣' or carta == '10♥' or carta == '10♠' or carta == '10♦':
        return carta[2]
    else:
        return carta[1]

def extrai_valor(carta):
    if carta == '10♣' or carta == '10♥' or carta == '10♠' or carta == '10♦':
        return '10'
    else:
        return carta[0]


def lista_movimentos_possiveis(baralho):
    if baralho[0]:
        return []
    else:
        
      for i in range(1,len(baralho)):

        if (baralho[i] == '10' and baralho[i - 1] == '10') or (baralho[i + 2] == '10' and baralho[i - 1] == '10'):
          return [1]

        valor1 = baralho[i-1][0]
        naipe1 = baralho[i-1][1]

        valor3 = baralho[i-1][0]
        naipe3 = baralho[i-1][1]


        else:

          (baralho[i] == valor1 or baralho[i] == naipe1) or (baralho[i + 2] == valor3 or baralho[i + 2] == naipe3)
          return [1]