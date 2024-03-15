# Exercício 03 - Gerenciamento de Contatos

# Desenvolva um programa em Python para gerenciar uma lista de contatos. O programa deve permitir ao usuário adicionar novos contatos, remover contatos existentes, buscar por um contato pelo nome e exibir todos os contatos armazenados. Implemente as seguintes funcionalidades:

#     Crie um arquivo JSON para armazenar os contatos.
#     Permita que o usuário adicione um novo contato fornecendo nome, número de telefone e endereço de e-mail.
#     Permita que o usuário remova um contato existente fornecendo o nome do contato.
#     Permita que o usuário busque por um contato pelo nome.
#     Mostre todos os contatos armazenados no arquivo JSON.

import json

def add_contact(contacts):
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("E-mail: ")
    contact = {"Nome": name, "Telefone": phone, "E-mail": email}
    contacts.append(contact)
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contato adicionado com sucesso!")

def remove_contact(contacts):
    name = input("Nome: ")
    for contact in contacts:
        if contact["Nome"] == name:
            contacts.remove(contact)
            with open("contacts.json", "w") as file:
                json.dump(contacts, file)
            print("Contato removido com sucesso!")
            return
    print("Contato não encontrado!")

def search_contact():
    nome = input("Nome: ")
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
        for contact in contacts:
            if contact["Nome"] == nome:
                print(contact)
                return
    print("Contato não encontrado!")

def print_contacts():
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
        for contact in contacts:
            print(contact)

def main():
    contacts = []

    while True:
        print("\nSelecione uma opção:")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Mostrar contatos")
        print("5. Sair")

        choice = input("Opcão: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            remove_contact(contacts)
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print_contacts()
        elif choice == "5":
            break
        else:
            print("Opcão inválida. Tente novamente.")


main()