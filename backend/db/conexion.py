import psycopg2

def conectar():
    return psycopg2.connect(
        dbname="seguridad",
        user="admin",
        password="tu_password",
        host="localhost"
    )
