# Exercício 01 - Lista de Tarefas em Python

# Você foi contratado para desenvolver um programa em Python que simule uma lista de tarefas, onde o usuário pode adicionar, remover, visualizar e limpar tarefas da lista. O programa deve oferecer um menu interativo para que o usuário possa escolher entre as diferentes opções disponíveis.

# Você deve implementar uma classe TodoList com os seguintes métodos:

#     __init__(self): Inicializa a lista de tarefas vazia.
#     add_task(self, task): Adiciona uma nova tarefa à lista.
#     remove_task(self, task): Remove uma tarefa específica da lista, se existir.
#     show_tasks(self): Mostra todas as tarefas atualmente na lista.
#     clear_tasks(self): Remove todas as tarefas da lista.

# Além disso, você deve implementar uma função main() que cria uma instância da classe TodoList e oferece um menu interativo para o usuário interagir com a lista de tarefas. O menu deve incluir as seguintes opções:

#     Adicionar Tarefa
#     Remover Tarefa
#     Mostrar Tarefas
#     Limpar Lista de Tarefas
#     Sair

# O programa deve continuar em execução até que o usuário escolha a opção de sair.

# Por favor, implemente a classe TodoList e a função main() conforme descrito acima. Certifique-se de lidar com entradas inválidas do usuário de forma adequada. Use POO para este exercício. Além disso, faça a criação de testes para isso com Pytest.
class Task: 
    def __init__(self, task):
        self.task = task
    
    def __str__(self):
        return self.task

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        for i in self.tasks:
            if i.task == task:
                self.tasks.remove(i)

    def show_tasks(self):
        if not self.tasks:
            print("Nenhuma tarefa encontrada.")
        else:
            print("Tarefas: ")
            for task in self.tasks:
                print(f"- {task}")

    def clear_tasks(self):
        self.tasks = []

def menu():
    print("\nSelecione uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Mostrar Tarefas")
    print("4. Limpar Lista de Tarefas")
    print("5. Sair")

def main():
    todo_list = TodoList()

    while True:
        menu()
        choice = input("Opcão: ")

        if choice == "1":
            task = input("Tarefa: ")
            task = Task(task)
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Tarefa: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            todo_list.clear_tasks()
        elif choice == "5":
            break
        else:
            print("Opcão inválida. Tente novamente.")

main()