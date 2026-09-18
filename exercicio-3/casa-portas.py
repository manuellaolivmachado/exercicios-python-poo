class Porta:
    def __init__(self):
        self.estado = "Fechada"

    def abrir(self):
        self.estado = "Aberta"

    def fechar(self):
        self.estado = "Fechada"


class Casa:
    def __init__(self):
        self.nome = input("Digite o nome da casa: ")
        self.porta1 = Porta()
        self.porta2 = Porta()
        self.porta3 = Porta()

    def exibir(self):
        print(f"\nEstado das portas da {self.nome}:")
        print(f"Porta 1: {self.porta1.estado}")
        print(f"Porta 2: {self.porta2.estado}")
        print(f"Porta 3: {self.porta3.estado}")


casa1 = Casa()

continuar = "sim"

while continuar == "sim":

    porta = int(input("\nQual porta deseja alterar? (1, 2 ou 3): "))
    acao = input("Deseja abrir ou fechar? ")

    if porta == 1:
        if acao == "abrir":
            casa1.porta1.abrir()
        elif acao == "fechar":
            casa1.porta1.fechar()

    elif porta == 2:
        if acao == "abrir":
            casa1.porta2.abrir()
        elif acao == "fechar":
            casa1.porta2.fechar()

    elif porta == 3:
        if acao == "abrir":
            casa1.porta3.abrir()
        elif acao == "fechar":
            casa1.porta3.fechar()

    continuar = input("Deseja alterar outra porta? (sim/não): ")


casa1.exibir()
