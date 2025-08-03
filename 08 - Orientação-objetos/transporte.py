from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, modelo):
        self._modelo = modelo  

    @property
    def modelo(self):
        return self._modelo

    @abstractmethod
    def mover(self):
        pass


class Carro(Transporte):
    def __init__(self, modelo, numero_portas):
        super().__init__(modelo)
        self.numero_portas = numero_portas

    def mover(self):
        print(f"O carro {self.modelo} está dirigindo pelas ruas.")


class Bicicleta(Transporte):
    def __init__(self, modelo, marchas):
        super().__init__(modelo)
        self.marchas = marchas

    def mover(self):
        print(f"A bicicleta {self.modelo} está pedalando pela ciclovia.")


class Aviao(Transporte):
    def __init__(self, modelo, capacidade_passageiros):
        super().__init__(modelo)
        self.capacidade_passageiros = capacidade_passageiros

    def mover(self):
        print(f"O avião {self.modelo} está voando pelos céus.")
