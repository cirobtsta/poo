class Bicicleta:
    # class = keyword, reservada para criar uma classe
    def __init__(self, cor, modelo, ano, valor):
        #def __init__ = método construtor
        #self = representa a instância de um objeto, explicita
        self.cor = cor
        #self. = atributo da classe
        self.modelo = modelo
        self.ano = ano
        self.valor =  valor


b1 = Bicicleta("preta", "cannondale", 2022, 16000)

print b1