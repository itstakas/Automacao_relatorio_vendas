#CRUDE

from struct import pack_into

import pandas as pd
from numpy.f2py.crackfortran import usermodules

import mysql.connector

tabela = pd.read_csv("../Content/e91da71a-5b6e-4a07-8584-707fd264ac45.csv")
tabela2 = pd.read_excel("../Content/Planilha1.xlsx")

print("===================== VENDAS CRM ===================")
print(tabela.head())
print("===================== VENDAS SISTEMA ===================")
print(tabela2.head())