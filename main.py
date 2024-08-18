import random
from os import system, name

#função para limpar a tela do terminal
def limpa_tela():

  if name == 'nt':
    _= system('cls')
  else:
    _= system('clear')


def game():

  limpa_tela()

  print("\nBem-vindo(a) ao jogo da forca!")
  print("Adivinhe a palavra abaixo:\n")

  #lista de palavras
  palavras = ['ateez','riize','aespa','nct dream','twice']

  #escolha aleatoria das palavras
  palavra = random.choice(palavras)

  #list comprehension
  letras_descobertas = ['_' for letra in palavra]

  chances = 6

  letras_erradas = []

  while chances > 0:
    print(" ".join(letras_descobertas))
    print("\nChances restantes:", chances)
    print("Letras erradas:", " ".join(letras_erradas))

    tentativa = input("\nDigite uma letra: ".lower()) #vai sempre entender que a letra digitada eh minuscula

    if tentativa in palavra:
      i = 0

      for letra in palavra:
        if tentativa == letra:
          letras_descobertas[i] = letra
        i +=1
    else:
      chances -= 1
      letras_erradas.append(tentativa)

    if "_" not in letras_descobertas:
      print("\nVocê venceu, a palavra era:", palavra)
      break
  if "_" in letras_descobertas:
    print("\nVocê perdeu, a palavra era:", palavra)


if __name__ == '__main__':
  game()
  print("\nObrigado por jogar!")
