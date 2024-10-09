class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
         raise NotImplementedError("Metodo som não implementado")

class Cachorro(Animal):
    def som(self):
        return f"{self.nome} Au au!"

class Gato(Animal):
    def som(self):
        return f"{self.nome} Miau!"


def emitir_sons(animais):
    for animal in animais:
        print(animal.som())


meu_cachorro = Cachorro("Bolinha")
meu_gato = Gato("Garfield")
outro_gato = Gato("Rex")

animais = [meu_cachorro, meu_gato, outro_gato]
emitir_sons(animais)