numeros = []

for i in range(10):
  numero = int(input(f"Digite o número {i+1}: "))
  numeros.append(numero)

maior = numeros[0]
menor = numeros[0]
for numero in numeros:
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")