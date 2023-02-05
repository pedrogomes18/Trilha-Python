class Bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = 18
    
    def buzinar(self):
        print("PIIIIIII")
    
    def parar(self):
        print("Parando...")

    def correr(self):
        print("correr")

    def trocar_marcha(self):
        print("Marcha alterada")

    def __str__(self):
        #return f"Bicicleta: {self.cor}, {self.ano}, {self.modelo}, {self.valor}"

        #Automatização da class
        return f"{self.__class__.__name__}:\n {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



b1 = Bicicleta("vermelha", "caloi", 2013, 6000)
b1.correr()
b1.buzinar()
b1.parar()

print(b1.cor, b1.modelo)
print(b1.__str__())
        