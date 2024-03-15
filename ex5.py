# Exercício 05 - Sistema de Gerenciamento de Veículos

# Você foi contratado para desenvolver um sistema de gerenciamento de veículos para uma empresa de aluguel de carros. O sistema deve ser capaz de lidar com diferentes tipos de veículos, como carros, motos e caminhões. Cada tipo de veículo possui características específicas, como modelo, ano, placa e preço de aluguel por dia.

# Você deve implementar um sistema que permita ao usuário adicionar novos veículos, listar todos os veículos disponíveis, calcular o valor do aluguel com base no tipo de veículo e na duração do aluguel, e encontrar veículos disponíveis para aluguel em uma determinada data.

# Implemente as seguintes classes:

#     Veiculo (classe abstrata): Esta classe representa um veículo genérico e deve conter os seguintes métodos abstratos:
#         calcular_aluguel(self, dias: int) -> float: Método abstrato para calcular o valor do aluguel do veículo com base no número de dias de aluguel.
#         __str__(self) -> str: Método para retornar uma representação em string do veículo.
#     Carro: Representa um carro e deve herdar da classe Veiculo. Deve conter os seguintes atributos:
#         modelo: Modelo do carro.
#         ano: Ano de fabricação do carro.
#         placa: Placa do carro.
#         preco_por_dia: Preço de aluguel por dia do carro. Implemente os métodos necessários.
#     Moto: Representa uma moto e deve herdar da classe Veiculo. Deve conter os mesmos atributos que Carro e implementar os métodos abstratos.
#     Caminhao: Representa um caminhão e deve herdar da classe Veiculo. Deve conter os mesmos atributos que Carro e implementar os métodos abstratos.
#     SistemaAluguel: Esta classe deve conter métodos estáticos para lidar com o sistema de aluguel, como adicionar veículos, listar veículos disponíveis, encontrar veículos disponíveis para aluguel em uma determinada data, etc.

# Implemente o programa principal que permite ao usuário interagir com o sistema de gerenciamento de veículos, fornecendo um menu de opções para realizar diferentes operações.
from abc import ABC
class Veiculo(ABC):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.preco_por_dia = preco_por_dia

    def calcular_aluguel(self, dias):
        pass

    def __str__(self):
        pass

class Carro(Veiculo):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        super().__init__(modelo, ano, placa, preco_por_dia)
        data_alugueis = [] 

    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia
    def __str__(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Placa: {self.placa}, Preço por dia: {self.preco_por_dia}, Data de aluguel: {self.data_aluguel}"

class Moto(Veiculo):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        super().__init__(modelo, ano, placa, preco_por_dia)
        data_alugueis = [] 

    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia

    def __str__(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Placa: {self.placa}, Preço por dia: {self.preco_por_dia}, Data de aluguel: {self.data_aluguel}"
    
class Caminhao(Veiculo):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        super().__init__(modelo, ano, placa, preco_por_dia)
        data_alugueis = [] 

    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia

    def __str__(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano}, Placa: {self.placa}, Preço por dia: {self.preco_por_dia}, Data de aluguel: {self.data_aluguel}"
    
class Gerenciador():
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def encontrar_veiculos_disponiveis(self, data):
        pass

    def alugar_veiculo(self, veiculo, data):
        pass