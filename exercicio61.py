notas = []

for i in range(4):
  nota = float(input(f"Digite a nota {i+1}: "))
  notas.append(nota)

media = sum(notas) / len(notas)

print(f"Média das notas: {media:.2f}")

print("Notas maiores que a média:")
for nota in notas:
  if nota > media:
    print(nota)