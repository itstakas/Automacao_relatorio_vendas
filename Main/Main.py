#CRUDE
from struct import pack_into

import pandas as pd
from numpy.f2py.crackfortran import usermodules

print ("Panda esta funcionando")

import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="teste_python"
    )

    if conexao.is_connected():
        print("Deu certo a conexão")
        print("Banco: ", conexao.database)

except mysql.connector.Error as erro:
    print("Erro ao conectar ", erro)

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada")
