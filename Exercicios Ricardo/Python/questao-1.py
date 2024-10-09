class Carro:
    def __init__(self, marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(
            self.marca,
            self.modelo,
            self.ano
        )


carro1 = Carro('Ferrari', 'italia', 2020)
carro2 = Carro('Chevrolet', 'onix', 2019)

carro1.exibir()
carro2.exibir()