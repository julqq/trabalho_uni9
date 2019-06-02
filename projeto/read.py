import sqlite3
def visualizar_cadastros():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
    SELECT * FROM clientes;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
