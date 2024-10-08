nomes_alunos = []
while True:
  nome = input("Digite o nome de um aluno (ou 'fim' para finalizar): ")
  if nome.lower() == "fim":
    break
  nomes_alunos.append(nome)
print("\nNomes dos alunos do 2DS:")
for nome in nomes_alunos:
  print(nome)