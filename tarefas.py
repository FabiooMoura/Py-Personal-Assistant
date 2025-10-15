# Gerenciamento de tarefas

tarefas = []

def adicionar_tarefa(descricao: str):
    tarefas.append(descricao)
    print(f"Tarefa adicionada: {descricao}")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa pendente.")
    else:
        print("Suas tarefas:")
        for i, t in enumerate(tarefas, start=1):
            print(f"{i}. {t}")

def remover_tarefa(indice: int):
    if 0 < indice <= len(tarefas):
        removida = tarefas.pop(indice -1)
        print(f"Tarefa removida: {removida}")
    else:
        print("Índice inválido")





