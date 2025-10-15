# Acompanhamento de hábitos

habitos = {"Ler": False, "Estudar python": False, "Beber água": False}

def marcar_habito(nome:str): 
    if nome in habitos:
        habitos[nome] = True
        print(f"Hábito '{nome}' marcado como concluído!")
    else:
        print("Esse hábito não existe.")

def progresso():
    concluídos = sum(1 for v in habitos.values() if v)
    total = len(habitos)
    print(f"Progresso de hoje: {concluídos}/{total} hábitos concluídos.")

