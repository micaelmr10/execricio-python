intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
numero = int(input("Digite um número positivo (ou um número negativo para sair): "))
while numero >= 0:
  if 0 <= numero <= 25:
    intervalo1 += 1
  elif 26 <= numero <= 50:
    intervalo2 += 1
  elif 51 <= numero <= 75:
    intervalo3 += 1
  elif 76 <= numero <= 100:
    intervalo4 += 1
  else:
    print("Número inválido. Por favor, digite um número entre 0 e 100.")
  numero = int(input("Digite um número positivo (ou um número negativo para sair): "))
print("\nContagem de números em cada intervalo:")
print("Intervalo [0-25]:", intervalo1)
print("Intervalo [26-50]:", intervalo2)
print("Intervalo [51-75]:", intervalo3)
print("Intervalo [76-100]:", intervalo4)