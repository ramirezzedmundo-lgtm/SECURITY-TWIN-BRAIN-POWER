import time
import uuid

def generar_token():
    return str(uuid.uuid4())

def rotar_tokens(intervalo=10, duracion=2100):  # 35 min = 2100 seg
    inicio = time.time()
    while time.time() - inicio < duracion:
        token = generar_token()
        print(f"Token rotado: {token}")
        time.sleep(intervalo)
