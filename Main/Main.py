#CRUDE

from struct import pack_into

import pandas as pd
from numpy.f2py.crackfortran import usermodules
import mysql.connector
import streamlit as st
from dashboard import main

caminho_csv = "../Content/e91da71a-5b6e-4a07-8584-707fd264ac45.csv"
caminho_excel = "../Content/Planilha1.xlsx"

df_csv = pd.read_csv(caminho_csv, sep=";") #arquivo csv tem ue ter esse "sep=;" ou "sep=." pq se n fica tudo numa linha so
df_excel = pd.read_excel(caminho_excel)

colunas_csv_uteis = ['Cliente', 'Vendedor']
df_csv = df_csv[colunas_csv_uteis]
df_csv = df_csv.dropna()

colunas_excel_uteis = ['UNIDADE', 'CONTRATO', 'NOME', 'DATA_CONTRATO', 'VENDEDOR', 'REGIAO', 'PLANO',
                       'DIA_PAGAMENTO', 'ROTA', 'VALOR_ADESAO', 'DATA_ADESAO', 'CONCORRENTE', 'SITUACAO'
]
df_excel = df_excel[colunas_excel_uteis]
df_excel = df_excel.dropna(subset=['PLANO'])
df_excel = df_excel.fillna("N/A")  # td que for NaN ele troca por N/A, dai n da erro
df_excel['DATA_CONTRATO'] = pd.to_datetime(df_excel['DATA_CONTRATO'], errors='coerce')
df_excel['DATA_ADESAO'] = pd.to_datetime(df_excel['DATA_ADESAO'], errors='coerce')

df_excel['VENDEDOR_TELE'] = None

for _, row_csv in df_csv.iterrows():
    mask = df_excel['NOME'] == row_csv['Cliente']
    df_excel.loc[mask, 'VENDEDOR_TELE'] = row_csv['Vendedor']
onnect(
    host="l
conexao = mysql.connector.cocalhost",
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
    situação VARCHAR(100),
    vendedor_tele VARCHAR(100)
);

"""
cursor.execute(comando_sql) #Roda o que eu escrevi
conexao.commit()

for _, linha in df_excel.iterrows():
    cursor.execute("SELECT contrato FROM relatorio_vendas WHERE contrato = %s", (linha['CONTRATO'],))
    resultado = cursor.fetchone()

    valores = (
        linha['UNIDADE'], linha['CONTRATO'], linha['NOME'],
        linha['DATA_CONTRATO'], linha['VENDEDOR'], linha['REGIAO'],
        linha['PLANO'], linha['DIA_PAGAMENTO'], float(str(linha['VALOR_ADESAO']).replace(",",".")), linha['DATA_ADESAO'],
        linha['CONCORRENTE'], linha['SITUACAO'], linha['VENDEDOR_TELE']
    )

print(linha)
if resultado:
    sql = """
        UPDATE relatorio_vendas SET
            unidade = %s,
            contrato = %s,
            nome = %s,
            data_contrato = %s,
            vendedor =%s,
            regiao = %s, 
            plano = %s,
            dia_pagamento = %s,
            valor_adesao = %s,
            data_adesao = %s,
            concorrente = %s,
            situação = %s,
            vendedor_tele = %s
        WHERE contrato = %s
    """
    valores = (
        linha['UNIDADE'], linha['CONTRATO'], linha['NOME'],
        linha['DATA_CONTRATO'], linha['VENDEDOR'], linha['REGIAO'],
        linha['PLANO'], linha['DIA_PAGAMENTO'], float(str(linha['VALOR_ADESAO']).replace(",",".")),
        linha['DATA_ADESAO'], linha['CONCORRENTE'], linha['SITUACAO'], linha['VENDEDOR_TELE'], linha['CONTRATO']
    )
    cursor.execute(sql, valores)
else:
    print(linha)
    sql = """
        INSERT INTO relatorio_vendas
        (unidade, contrato, nome, data_contrato, vendedor, regiao, plano,
        dia_pagamento, valor_adesao, data_adesao, concorrente, situação, vendedor_tele)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        linha['UNIDADE'], linha['CONTRATO'], linha['NOME'],
        linha['DATA_CONTRATO'], linha['VENDEDOR'], linha['REGIAO'],
        linha['PLANO'], linha['DIA_PAGAMENTO'], float(str(linha['VALOR_ADESAO']).replace(",",".")),linha['DATA_ADESAO'],
        linha['CONCORRENTE'], linha['SITUACAO'], linha['VENDEDOR_TELE']
    )

    cursor.execute(sql, valores)

conexao.commit() #Commita/salva no banco de verdade
cursor.close() #fecha o cursor pra liberar memoria
conexao.close() #fecha a conexao com o bd

print("Tabela criada com sucesso") #Confecção de eENDEDORrros
print(f"Processo concluído! {len(df_excel)} registros processados.")

if __name__ == "__main__":
    main()
