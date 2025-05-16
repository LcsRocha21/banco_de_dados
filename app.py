import streamlit as st
import mysql.connector
import pandas as pd

# Título
st.title("📋 Lista de Clientes")

# Conectar ao banco de dados
def conectar():
    return mysql.connector.connect(
        host="localhost",      # ou o IP do servidor
        user="root",           # seu usuário MySQL
        password="1210",  # substitua pela sua senha
        database="new_schema"  # substitua pelo nome do seu banco
    )

# Obter dados da tabela
def carregar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, email, idade FROM clientes")
    dados = cursor.fetchall()
    colunas = ["ID", "Nome", "Email", "Idade"]
    df = pd.DataFrame(dados, columns=colunas)
    cursor.close()
    conexao.close()
    return df

# Mostrar tabela na interface
try:
    df_clientes = carregar_clientes()
    st.dataframe(df_clientes)
except Exception as e:
    st.error(f"Erro ao conectar ou buscar dados: {e}")
