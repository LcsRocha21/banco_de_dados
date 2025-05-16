import streamlit as st
import mysql.connector
import pandas as pd

# Título
st.title("📋 Lista de Clientes")

# Conectar ao banco de dados
def conectar():
    return mysql.connector.connect(
        host="192.168.68.100",       # IP correto da máquina com MySQL
        user="usuario_remoto",       # usuário remoto criado no MySQL
        password="3015",             # sua senha
        database="new_schema"        # nome do banco
    )

# Obter dados da tabela
def carregar_clientes():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, idade FROM clientes")
        dados = cursor.fetchall()
        colunas = ["ID", "Nome", "Email", "Idade"]
        df = pd.DataFrame(dados, columns=colunas)
        cursor.close()
        conexao.close()
        return df
    except mysql.connector.Error as err:
        st.error(f"Erro de conexão com MySQL: {err}")
        return pd.DataFrame()

# Mostrar tabela na interface
df_clientes = carregar_clientes()

if not df_clientes.empty:
    st.dataframe(df_clientes)
else:
    st.warning("Nenhum dado foi retornado da tabela.")
