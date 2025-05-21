import streamlit as st
import pandas as pd
import mysql.connector
from numpy.f2py.crackfortran import usermodules

def main():

def carregar_dados():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bdvendas"
    )

    query = "SELECT * FROM relatorio_vendas"
    df = pd.read_sql(query, conexao)
    conexao.close()
    return df


st.set_page_config(page_title="Relatório de Vendas", layout="wide")
st.title("Relatório de Vendas")

df = carregar_dados()

col1, col2, col3 = st.columns(3)

unidades = df['unidade'].unique()
vendedores = df['vendedor'].unique()
regioes = df['regiao'].unique()

unidade_filtro = col1.selectbox("Filtrar por unidade", ["Todas"] + list(unidades))
vendedor_filtro = col2.selectbox("Filtrar por vendedor", ["Todas"] + list(vendedores))
regioes_filtro = col3.selectbox("Filtrar por regiões", ["Todas"] + list(regioes))

df_filtrado = df.copy()

if unidade_filtro != "Todas":
    df_filtrado = df_filtrado[df_filtrado['unidade'] == unidade_filtro]

if vendedor_filtro != "Todas":
    df_filtrado = df_filtrado[df_filtrado['vendedor'] == vendedor_filtro]

if regioes_filtro != "Todas":
    df_filtrado = df_filtrado[df_filtrado['regioes'] == regioes_filtro]

st.dataframe(df_filtrado)

st.markdown("Resumo dos dados")
col1, col2, col3 = st.columns(3)
col1.metric("Total de contratos", len(df_filtrado))
col2.metric("Vendas únicas", df_filtrado['contrato'].unique())
col3.metric("Total em Adesões", f"R$ {df_filtrado['valor_adesao'].sum():,2f}".replace(",","x").replace(".",",").replace("X", "."))
