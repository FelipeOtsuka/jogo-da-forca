from frutas import lista
import random
c = random.choice(lista)	
chance = 0
pontos = 0
palavra = c
t = len(palavra) + 3
s = len(palavra)
while chance<t and pontos<s:
  tentativa = str(input("chute uma letra de uma fruta"))
  chance = chance + 1
  if tentativa in palavra:
    pontos = pontos + 1
    x = palavra.index(tentativa)
    del palavra[x]
    print("parabens voce acertou, agora voce possuí", pontos, "pontos.E usou", chance,"chances")
  else:
    print("você errou, mas aqui vai uma dica: é uma fruta pequena e redonda")
  if pontos == s:
    print("parabens voce ganhou")
  if chance == t:
    print("voce perdeu mas não se desanime, voce pode tentar de novo")