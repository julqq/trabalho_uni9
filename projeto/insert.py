import sqlite3
from datetime import datetime

def inserir_cadastros():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    while True :
        p_nome = input('Nome: ')
        p_nascimento = input('Data de Nascimento: ')
        p_cpf = input('CPF: ')
        p_email = input('Email: ')
        p_fone = input('Fone: ')
        p_cidade = input('Cidade: ')
        p_uf = input('UF: ')
        p_criado_em = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


        #  inserindo dados na tabela
        cursor.execute("""
        INSERT INTO clientes (nome, nascimento, cpf, email, fone, cidade, uf, criado_em)
        VALUES (?,?,?,?,?,?,?,?)
        """, (p_nome, p_nascimento, p_cpf, p_email, p_fone, p_cidade, p_uf, p_criado_em))

        conn.commit()

        print('Dados inseridos com sucesso.')

        condition = input('Deseja inserir mais um cadastro? [S/N]').upper()
        if condition == 'S':
            continue
        else:
            print('Sistema de cadrastos finalizado!')
            break

    conn.close()
