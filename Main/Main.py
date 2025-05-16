#CRUDE

from struct import pack_into

import pandas as pd
from numpy.f2py.crackfortran import usermodules

import mysql.connector

caminho_csv = "../Content/e91da71a-5b6e-4a07-8584-707fd264ac45.csv"
caminho_excel = "../Content/Planilha1.xlsx"

df_csv = pd.read_csv(caminho_csv)
df_excel = pd.read_excel(caminho_excel)

df_final = pd.concat([df_csv, df_excel], ignore_index=True)
df_final.to_excel("arquivo_unificado.xlsx", index=False)

print("Aquivo Excel foi salvo")


