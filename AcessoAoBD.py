import psycopg2

#QUERYS DO BD
create_table_query = "CREATE TABLE cantoras (codigo SERIAL PRIMARY KEY, nome VARCHAR(100), quantidadeAlbuns INT, media_por_musica NUMERIC(9,2), dataProximo_lancamento DATE)"
insertQuery = "INSERT INTO cantoras (nome, quantidadeAlbuns, media_por_musica, dataProx_lancamento) VALUES (%s, %s, %s, %s)"
updateNomeQuery = "UPDATE cantoras SET nome = %s WHERE codigo = %s"
updateAlbunsQuery = "UPDATE cantoras SET quantidadeAlbuns = %s WHERE codigo = %s"
updateMediaQuery ="UPDATE cantoras SET media_por_musica = %s WHERE codigo = %s"
updateDataQuery = "UPDATE cantoras SET dataProx_lancamento = %s WHERE codigo = %s"
deleteQuery = "DELETE FROM cantoras WHERE codigo = %s"
selectUmaQuery = "SELECT * FROM cantoras WHERE codigo = %s"
selectGeralQuery = "SELECT * FROM cantoras ORDER BY nome ASC"

dbname = "gravadora"
user = "postgres"
password="******"
host="localhost"
port = "5432"

connection = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port)
cursor = connection.cursor()

def createTable():
    cursor.execute(createTable)
    connection.commit
    print("Tabela criada com sucesso!")

def insert(nome, quantidadeAlbuns, media_por_musica, dataProx_lancamento):
    cursor.execute(insertQuery, (nome, quantidadeAlbuns, media_por_musica, dataProx_lancamento))
    connection.commit()
    print("Cantora %s inserida com sucesso!" %nome)

def updateAlbuns(codigo, novaQuant):
    cursor.execute(updateAlbunsQuery, (novaQuant, codigo))
    connection.commit()
    print("Número de albuns atualizado com sucesso!")

def updateMedia(codigo, novaMedia):
    cursor.execute(updateMediaQuery,(novaMedia, codigo))
    connection.commit()
    print("Média atualizada com sucesso!")

def updateData(codigo, novaData):
    cursor.execute(updateDataQuery,(novaData, codigo))
    connection.commit()
    print("Data atualizada com sucesso!")

def updateNome(codigo, novoNome):
    cursor.execute(updateNomeQuery, (novoNome, codigo))
    connection.commit()
    print("Nome atualizado com sucesso!")

def delete(codigo):
    cursor.execute(deleteQuery,(codigo,))
    connection.commit()
    print("Cantora de codigo = %s deletada com sucesso!" %codigo)
def selectUma(codigo):
    cursor.execute(selectUmaQuery, (codigo,))
    busca = cursor.fetchall()
    if busca:
        print("Artista encontrada:")
        for i in busca:
            print("Codígo: ", busca[0][0], "| Nome: ", busca[0][1], "| Quantidade de álbuns: ", busca[0][2], "| Média arrecadada p/ música: R$", busca [0][3], " | Data prox. laçamento: ", busca [0][4])
    else: 
        print("Nenhuma cantora de codigo %s foi encontrada" %codigo)

def selectGeral():
    cursor.execute(selectGeralQuery)
    busca = cursor.fetchall()
    if busca:
        print("Registros encontrados:")
        for registro in busca:
            codigo, nome, quantidade_albuns, media_por_musica, data_prox_lancamento = registro
            print("Código:", codigo, "| Nome:", nome, "| Quantidade de álbuns:", quantidade_albuns, "| Média arrecadada por música: R$", media_por_musica, "| Data próximo lançamento:", data_prox_lancamento)
    else: 
        print("Nenhuma cantora foi encontrada")
