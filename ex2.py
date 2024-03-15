# Exercício 02 - Processamento de Lista de Compras

# Você foi encarregado de desenvolver um programa em Python para gerenciar uma lista de compras de supermercado. O programa deve permitir ao usuário adicionar itens à lista, remover itens existentes, mostrar todos os itens da lista e calcular o total de gastos com base nos preços dos itens. Implemente as seguintes funcionalidades:

#     Permita que o usuário adicione itens à lista de compras, especificando o nome do item e o preço.
#     Permita que o usuário remova itens da lista de compras, especificando o nome do item.
#     Mostre todos os itens atualmente na lista de compras.
#     Calcule e mostre o total de gastos com base nos preços dos itens na lista.

# Use POO para este exercício. Além disso, faça a criação de testes para isso com Pytest

class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - R${self.price:.2f}"
    
class ShoppingList():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)

    def show_items(self):
        if not self.items:
            print("Nenhum item encontrado.")
        else:
            print("Itens:")
            for item in self.items:
                print(f"- {item}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

def menu():
    print("\nSelecione uma opção:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Mostrar itens")
    print("4. Calcular total")
    print("5. Sair")

def validate_input():
    while True:
        try:
            price = float(input("Preço: "))
            return price
        except ValueError:
            print("Opcão inválida. Tente novamente.")

def main():
    shopping_list = ShoppingList()

    while True:
        menu()
        choice = input("Opcão: ")

        if choice == "1":
            name = input("Nome do item: ")
            price = validate_input()
            item = Item(name, price)
            shopping_list.add_item(item)
        elif choice == "2":
            name = input("Nome do item: ")
            shopping_list.remove_item(name)
        elif choice == "3":
            shopping_list.show_items()
        elif choice == "4":
            print(f"Total: R${shopping_list.calculate_total():.2f}")
        elif choice == "5":
            break
        else:
            print("Opcão inválida. Tente novamente.")


main()