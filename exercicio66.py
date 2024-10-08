nomes = []
notas = []
for i in range(4):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nomes.append(nome)
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas_aluno.append(nota)
    media = sum(notas_aluno) / 4
    notas_aluno.append(media)
    notas.append(notas_aluno)
for i in range(4):
    print(f"Aluno: {nomes[i]}")
    for j in range(4):
        print(f"Nota {j+1}: {notas[i][j]:.2f}")
    print(f"Média: {notas[i][4]:.2f}")