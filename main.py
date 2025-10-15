from tarefas import adicionar_tarefa, listar_tarefas, remover_tarefa
from habitos import marcar_habito, progresso
from saude import calcular_imc
from utilidades import saudacao, gerar_senha

print("=== Personal Assistant ===")
print(saudacao())

while True:
    print("""
    [1] Gerenciar tarefas
    [2] Marcar hábitos
    [3] Calcular IMC
    [4] Gerar senha aleatória
    [0] Sair 
    """)
    opcao = input("Escolha: ")

    if opcao == "1":
        listar_tarefas()
        nova = input("Adicionar nova tarefa(ou Enter para pular): ")
        if nova:
            adicionar_tarefa(nova)
    elif opcao == "2":
        nome = input("Qual hábito você cumpriu?")
        marcar_habito(nome)
        progresso()
    elif opcao == "3":
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        imc, cat = calcular_imc(peso, altura)
        print(f"IMC: {imc} | Categoria: {cat}")
    elif opcao == "4":
        print("Senha gerada:", gerar_senha(10))
    elif opcao == "0":
        print("Saindo... até mais!")
        break
    else:
        print("Opção inválida.")

    