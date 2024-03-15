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
        self.data_alugueis = ['2022-01-01']

    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia
    def __str__(self):
        return f"Modelo: Ano: {self.ano}, Placa: {self.placa}, Preço por dia: {self.preco_por_dia}, Data de aluguel: {self.data_alugueis}"

class Moto(Veiculo):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        super().__init__(modelo, ano, placa, preco_por_dia)
        self.data_alugueis = ['2022-01-01']

    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia

    def __str__(self):
        return f"Modelo: Ano: {self.ano}, Placa: {self.placa}, Preço por dia: {self.preco_por_dia}, Data de aluguel: {self.data_alugueis}"
    
class Caminhao(Veiculo):
    def __init__(self, modelo, ano, placa, preco_por_dia):
        super().__init__(modelo, ano, placa, preco_por_dia)
        self.data_alugueis = ['2022-01-01']

    def calcular_aluguel(self, dias):
        return dias * self.preco_por_dia

    def __str__(self):
        return f"Ano: {self.ano}, Placa: {self.placa}, Preço por dia: {self.preco_por_dia}, Data de aluguel: {self.data_alugueis}"
    
class SistemaAluguel():
    @staticmethod
    def adicionar_veiculo(veiculo, veiculos):
        veiculos.append(veiculo)

    @staticmethod
    def encontrar_veiculos_disponiveis(data, veiculos):
        for veiculo in veiculos:
            if data not in veiculo.data_alugueis:
                print(veiculo)


    def alugar_veiculo(placa, veiculos, data, dias):
        for veiculo in veiculos:
            if veiculo.placa == placa:
                if data not in veiculo.data_alugueis:
                    veiculo.data_alugueis.append(data)
                    print({"Data de aluguel": data, "Dias de aluguel": dias, "Preço total": veiculo.calcular_aluguel(dias)})
                    print("Veiculo alugado com sucesso!")
                else:
                    print("Veiculo indisponível")
                    return
            else: 
                print("Veiculo indisponível")
                return

def main():
    veiculos = []
    while True:
        print("1 - Adicionar veiculo")
        print("2 - Encontrar veiculos disponíveis")
        print("3 - Alugar veiculo")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            modelo = input("Modelo: ")
            ano = int(input("Ano: "))
            placa = input("Placa: ")
            preco_por_dia = float(input("Preço por dia: "))
            tipo = input("Tipo: ")
            if tipo == "carro":
                veiculo = Carro(modelo, ano, placa, preco_por_dia)
            elif tipo == "moto":
                veiculo = Moto(modelo, ano, placa, preco_por_dia)
            elif tipo == "caminhão":
                veiculo = Caminhao(modelo, ano, placa, preco_por_dia)
            else:
                print("Tipo inválido. Tente novamente.")
                continue
            SistemaAluguel.adicionar_veiculo(veiculo, veiculos)

        elif opcao == "2":
            data = input("Data: ")
            SistemaAluguel.encontrar_veiculos_disponiveis(data, veiculos)
        
        elif opcao == "3":
            placa = input("Placa: ")
            data = input("Data: ")
            dias = int(input("Dias: "))
            SistemaAluguel.alugar_veiculo(placa, veiculos, data, dias)
        
        elif opcao == "4":
            break
        else:
            print("Opcão inválida. Tente novamente.")

main()