palavra = input("Digite uma palavra: ")
consoantes = []
vogais = "aeiouAEIOU"
for letra in palavra:
  if letra not in vogais:
    consoantes.append(letra)
print("Consoantes da palavra:", consoantes)