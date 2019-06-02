import insert, read, delete, viewtable, backup, recoverydb, createTable




#Comando para criar tabela
# createTable.criar_tabela()    

while True:
    
    print('Gerenciador de banco de dados.')


    print('Escolha a operação que deseja executar')
    
    print('[1] Castastrar.')
    print('[2] Visualizar cadastros.')
    print('[3] Deletar cadastro.')
    print('[0] Sair.')
    

    operation = int(input(': '))
    if operation == 1:
        insert.inserir_cadastros()
    elif operation == 2:
        read.visualizar_cadastros()
    elif operation == 3:
        delete.deletar_cadastro()
    elif operation == 0:
        print('Programa Finalizado.')
        break  
    else :
        print('Operação Invalida, Digite novamente.')

