import sqlite3

# (nome, nascimento, cpf, email, fone, cidade, uf, criado_em)

def criar_tabela():
        # conectando... ao banco de dados
        conn = sqlite3.connect('clientes.db')
        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("""
        CREATE TABLE clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nascimento TEXT NOT NULL,
                cpf     TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT NOT NULL,
                cidade TEXT NOT NULL,
                uf TEXT NOT NULL,
                criado_em DATE NOT NULL
        );
        """)

        print('Tabela criada com sucesso.')


        # desconectando...
        conn.close()
