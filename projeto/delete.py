import sqlite3


def deletar_cadastro():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    id_cliente = input('Insira o ID do cliente que sera deletado: ')

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM clientes
    WHERE id = ?
    """, (id_cliente,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()
