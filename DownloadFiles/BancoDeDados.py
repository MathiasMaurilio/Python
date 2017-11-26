import sqlite3

#Criando Banco de Dados
path = r'E:\Documents\DataBase'
conn = sqlite3.connect(path + r'\teste.db')

conn.close() #Se desconectar do banco de dados

"""
conn = sqlite3.connect('Endereço do banco de dados')
cursor = conn.execute('select * from "Nome da Tabela"')
rows = cursor.fetchall()

#Imprimir linha por linha
for row in rows:
    print(row)
"""