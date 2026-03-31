from fastapi import FastAPI
import psycopg2
import torch
from backend.ia.siamese import SiameseNet
from backend.seguridad.tokens import generar_token

app = FastAPI()

# --- Conexión a PostgreSQL ---
def conectar_db():
    return psycopg2.connect(
        dbname="seguridad",
        user="admin",
        password="tu_password",
        host="localhost"
    )

# --- Inicializar modelo ---
modelo = SiameseNet()

@app.get("/")
def root():
    return {"mensaje": "Sistema de Seguridad + Pentesting activo"}

@app.get("/diagnostico")
def diagnostico():
    # Ejemplo: datos simulados de pentesting
    reporte = {
        "ports": 2,
        "vulns": "XSS reflejado en login",
        "bruteForce": 500,
        "tokens": generar_token(),
        "damage": 0,
        "recommendations": "Cerrar puertos no usados y reforzar validación de entradas"
    }
    return reporte

@app.post("/guardar_modelo")
def guardar_modelo():
    conn = conectar_db()
    cursor = conn.cursor()
    for name, param in modelo.state_dict().items():
        cursor.execute(
            "INSERT INTO modelo (nombre, valores) VALUES (%s, %s) "
            "ON CONFLICT (nombre) DO UPDATE SET valores = %s",
            (name, param.detach().numpy().tolist(), param.detach().numpy().tolist())
        )
    conn.commit()
    conn.close()
    return {"status": "Modelo guardado en PostgreSQL"}
