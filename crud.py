import mysql.connector
''' 
CRUD é o ato de poder criar, ler, editar e deletar informações em um Banco de dados.
instalar o mysql workbench, e lembre-se q pra funcionar precisa do wampserver
instalar tb no terminal pip install mysql-connector-python.
'''
# conexao com o bd
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdpy'
)
cursor = conexao.cursor()

#cursor.close()
#conexao.close()

# CRUD

# CREATE
'''
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO Vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()  #edita o banco de dados

nome_produto = "toddynho"
valor = 15
comando = f'INSERT INTO Vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()  #edita o banco de dados

# READ
comando = f'SELECT * FROM Vendas'
cursor.execute(comando)
resultado = cursor.fetchall()  # lê o banco de dados
print(resultado)

# UPDATE
nome_produto = "toddynho"
valor = 6
comando = f'UPDATE Vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()   #edita o bd

# DELETE
nome_produto = "toddynho"
comando = f'DELETE FROM Vendas WHERE idVendas = 3'
cursor.execute(comando)
conexao.commit()    #edita o bd

comando = f'DELETE FROM Vendas WHERE idVendas = 3'
cursor.execute(comando)
conexao.commit()    #edita o bd
'''

# READ
comando = f'SELECT * FROM Vendas'
cursor.execute(comando)
resultado = cursor.fetchall()  # lê o banco de dados
print(resultado)