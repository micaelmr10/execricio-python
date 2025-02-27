``
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = {
            "Matemática": [],
            "Português": [],
            "História": [],
            "Geografia": [],
            "Ciências": []
        }

    def registrar_nota(self, matéria, nota):
        self.notas[máteria].append(nota)

    def calcular_média(self, matéria):
        return sum(self.notas[máteria]) / len(self.notas[máteria])

    def exibir_notas(self):
        print(f"Notas de {self.nome}:")
        for matéria, notas in self.notas.items():
            média = self.calcular_média(matéria)
            print(f"{matéria}: Média = {média:.2f}")
        print("-" * 30)

class Turma:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self, nome):
        aluno = Aluno(nome)
        self.alunos.append(aluno)

    def registrar_notas(self):
        for aluno in self.alunos:
            for matéria in aluno.notas.keys():
                for i in range(4):
                    nota = float(input(f"Digite a nota do {i+1}º bimestre de {matéria} para {aluno.nome}: "))
                    aluno.registrar_nota(matéria, nota)

    def exibir_turma(self):
        for aluno in self.alunos:
            aluno.exibir_notas()

def main():
    turma = Turma()

    while True:
        print("1. Cadastrar aluno")
        print("2. Registrar notas")
        print("3. Exibir turma")
        print("4. Sair")

        opção = input("Escolha uma opção: ")

        if opção == "1":
            nome = input("Digite o nome do aluno: ")
            turma.cadastrar_aluno(nome)
        elif opção == "2":
            turma.registrar_notas()
        elif opção == "3":
            turma.exibir_turma()
        elif opção == "4":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
