# Exercício 04 - Sistema de Gerenciamento de Produtos

# Desenvolva um programa em Python para gerenciar um sistema de estoque de produtos. O programa deve permitir ao usuário adicionar novos produtos, atualizar informações de produtos existentes, remover produtos e exibir todos os produtos disponíveis. Implemente as seguintes funcionalidades:

#     Crie um arquivo CSV para armazenar os produtos.
#     Permita que o usuário adicione um novo produto fornecendo nome, preço e quantidade inicial.
#     Permita que o usuário atualize o preço ou a quantidade disponível de um produto existente fornecendo o nome do produto e as informações atualizadas.
#     Permita que o usuário remova um produto existente fornecendo o nome do produto.
#     Mostre todos os produtos disponíveis no arquivo CSV.

import csv

def add_item():
    name = input("Nome do item: ")
    price = float(input("Preço: "))
    quantity = int(input("Quantidade: "))

    with open("products.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, price, quantity])

    print("Item adicionado com sucesso!")

def update_item():
    name = input("Nome do item: ")
    price = input("Preço: ")
    quantity = input("Quantidade: ")
    products = []
    updated = False
    with open("products.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                if price is not None:
                    row[1] = price
                if quantity is not None:
                    row[2] = quantity
                updated = True
            products.append(row)
        if updated:
            with open("products.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(products)
        else:
            print("não encontrado.")

def remove_item(products):
    name = input("Nome do item: ")
    products = []
    removed = False
    with open("products.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                removed = True
            else:
                products.append(row)
    if removed:
        with open("products.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(products)
        print("Item removido com sucesso!")
    else:
        print("Item não encontrado.")

def print_items(products):
    with open("products.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    products = []

    while True:
        print("\nSelecione uma opção:")
        print("1. Adicionar item")
        print("2. Atualizar item")
        print("3. Remover item")
        print("4. Mostrar itens")
        print("5. Sair")

        choice = input("Opcão: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            remove_item(products)
        elif choice == "4":
            print_items(products)
        elif choice == "5":
            break
        else:
            print("Opcão inválida. Tente novamente.")
main()