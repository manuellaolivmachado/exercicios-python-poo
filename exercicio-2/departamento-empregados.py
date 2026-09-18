class Empregado:
    def __init__(self):
        self.nome = input("Digite o nome do empregado: ")


class Departamento:
    def __init__(self):
        self.nome = input("Digite o nome do departamento: ")
        self.empregados = []

    def adicionar(self):
        novo_empregado = Empregado()
        self.empregados.append(novo_empregado)

    def listar(self):
        print(f"\nEmpregados do departamento {self.nome}:")

        for empregado in self.empregados:
            print(empregado.nome)


departamento1 = Departamento()

quantidade = int(input("Quantos empregados deseja adicionar? "))

for i in range(quantidade):
    departamento1.adicionar()

departamento1.listar()
