class Veiculo:

    def mover(self):

        print("O veículo está se movendo.")


class Carro(Veiculo):

    def mover(self):

        print("O carro está andando pela estrada.")


class Bicicleta(Veiculo):

    def mover(self):

        print("A bicicleta está pedalando pela ciclovia.")


carro1 = Carro()

bicicleta1 = Bicicleta()

carro1.mover()

bicicleta1.mover()
