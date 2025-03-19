

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = {}

    def adicionar_nota(self, materia, bimestre, nota):
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append((bimestre, nota))

    def calcular_media(self, materia):
        if materia in self.notas:
            return sum(nota for _, nota in self.notas[materia]) / len(self.notas[materia])
        return 0

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def exibir_notas(self):
        for aluno in self.alunos:
            print(aluno.nome)
            for materia in aluno.notas:
                media = aluno.calcular_media(materia)
                print(f"Média em {materia}: {media:.2f}")
            print("-" * 30)

def main():
    turma = Turma()

    while True:
        print("1. Cadastrar aluno")
        print("2. Registrar nota")
        print("3. Exibir notas")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do aluno: ")
            aluno = Aluno(nome)
            turma.adicionar_aluno(aluno)
        elif escolha == "2":
            nome = input("Digite o nome do aluno: ")
            aluno = next((a for a in turma.alunos if a.nome == nome), None)
            if aluno:
                materia = input("Digite o nome da matéria: ")
                bimestre = int(input("Digite o bimestre: "))
                nota = float(input("Digite a nota: "))
                aluno.adicionar_nota(materia, bimestre, nota)
            else:
                print("Aluno não encontrado.")
        elif escolha == "3":
            turma.exibir_notas()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

