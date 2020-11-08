import psycopg2




def conectar_postgres():
    try:
        conecta = psycopg2.connect(host="localhost",
                                   port="5432",
                                   database="musica",
                                   user="teste",
                                   password="teste")
        print("Conexão Estabelecida!")
        #
    except:
        print("Erro ao se conectar a base postgres!")
    return conecta

def valida_tabela(conecta, tabela):
    cursor = conecta.cursor()
    cursor.execute("select exists(select relname from pg_class where relname='{}');".format(tabela))
    tabela_existe = cursor.fetchone()[0]
    if tabela_existe is False:
        print('Tabela "{}" não existe. Será criada na base'.format(tabela))
        sql = 'create table musica (' \
              'id serial primary key,' \
              'nome varchar (100),' \
              'autor varchar (100),' \
              'genero varchar (50))'
        cursor.execute(sql)
        conecta.commit()
        print("Tabela criada")
    else:
        cursor.fetchall()
        cursor.close()


def insere_daddos(conecta, tabela):
    print(50 * "-" + "\n" + "Prova N2 - Atividade 2")
    print(50 * "-" + "\n" + "Cadastro de música base Postgres" + "\n" + 50 * "-")
    nome = input("Nome da música : ")
    autor = input("Nome do autor música : ")
    genero = input("Nome do gênero música : ")

    primeiro_dado_base = "insert into musica values (default, '{}', '{}', '{}')".format(nome, autor, genero)
    cursor = conecta.cursor()
    cursor.execute(primeiro_dado_base)
    conecta.commit()


    print("Musica {} do autor {}(gênero {}) foi adicionado ao MongoDB.".format(nome, autor, genero))



if __name__ == '__main__':
    conexao = conectar_postgres()
    valida_tabela(conexao, 'musica')
    insere_daddos(conexao, 'musica')
    conexao.close()