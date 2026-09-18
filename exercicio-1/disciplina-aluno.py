class Disciplina:
    def __init__(self):
        self.nome = input("Digite o nome da disciplina: ")


class Aluno:
    def __init__(self):
        self.nome = input("Digite seu nome: ")

    def inscrever(self, disciplina):
        print(f"{self.nome} se inscreveu na disciplina {disciplina.nome}!")


aluno1 = Aluno()
disciplina1 = Disciplina()

aluno1.inscrever(disciplina1)
