import pandas as pd

df_csv = pd.read_csv("../Content/e91da71a-5b6e-4a07-8584-707fd264ac45.csv", sep=";")
print("CSV - Colunas: ", df_csv.columns.tolist())

df_excel = pd.read_excel("../Content/Planilha1.xlsx")
print("Excel - Colunas: ", df_excel.columns.tolist())
