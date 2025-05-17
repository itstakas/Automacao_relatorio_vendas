#CRUDE

from struct import pack_into

import pandas as pd
from numpy.f2py.crackfortran import usermodules

import mysql.connector

caminho_csv = "../Content/e91da71a-5b6e-4a07-8584-707fd264ac45.csv"
caminho_excel = "../Content/Planilha1.xlsx"

df_csv = pd.read_csv(caminho_csv, sep=";") #arquivo csv tem que ter esse "sep=;" ou "sep=." pq se n fica tudo numa linha so
df_excel = pd.read_excel(caminho_excel)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="bdvendas"
)

cursor =  conexao.cursor()

comando_sql = """
CREATE TABLE IF NOT EXISTS relatorio_vendas (
    unidade VARCHAR(100),
    contrato VARCHAR(100),
    nome VARCHAR(255),
    data_contrato DATE,
    vendedor VARCHAR(100),
    regiao VARCHAR(100), 
    plano VARCHAR(100),
    dia_pagamento VARCHAR(100),
    valor_adesao DECIMAL(10,2),
    data_adesao DATE,
    concorrente VARCHAR(100),
    situação VARCHAR(100)    
);
"""
cursor.execute(comando_sql) #Roda o que eu escrevi
conexao.commit() #Commita/salva no banco de verdade

cursor.execute("DESCRIBE relatorio_vendas") #so pra mostrar a tabela criada mesmo, apagar depois
for linha in cursor.fetchall():
    print(linha)

cursor.close() #fecha o cursor pra liberar memoria
conexao.close() #fecha a conexao com o bd

print("Tabela criada com sucesso") #Confecção de erros


