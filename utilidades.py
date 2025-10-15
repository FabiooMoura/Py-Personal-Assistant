# Ferramentas gerais

import datetime
import random
import string

def saudacao():
    hora = datetime.datetime.now().hour
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
    
def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))
