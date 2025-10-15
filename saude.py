# Funções relacionadas à saúde

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    imc = round(imc, 1)
    if imc < 18.5:
        cat = "Abaixo do peso"
    elif imc < 25:
        cat = "Peso normal"
    elif imc < 30:
        cat = "Sobrepeso"
    else:
        cat = "Obesidade"
    return imc, cat
