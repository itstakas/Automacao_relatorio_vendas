#CRUDE

from struct import pack_into

import pandas as pd
from numpy.f2py.crackfortran import usermodules

import mysql.connector

caminho_csv = "../Content/e91da71a-5b6e-4a07-8584-707fd264ac45.csv"
caminho_excel = "../Content/Planilha1.xlsx"

df_csv = pd.read_csv(caminho_csv, sep=";")
df_excel = pd.read_excel(caminho_excel)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="bdvendas"
)




