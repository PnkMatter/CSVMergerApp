import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.set_page_config(page_title="Unificador de CSVs", layout="wide")

st.title("📊 Unificador de CSVs")

uploaded_files = st.file_uploader("Selecione os arquivos CSV", type="csv", accept_multiple_files=True)

if uploaded_files:
    dataframes = []

    for i, uploaded_file in enumerate(uploaded_files):
        df = pd.read_csv(uploaded_file, header=0)
        if i == 0:
            columns = df.columns  # Salva os nomes das colunas do primeiro
        else:
            df.columns = columns  # Garante que os outros tenham os mesmos nomes (caso estejam diferentes)
        dataframes.append(df)

    # Concatena todos os DataFrames, ignorando headers extras
    full_df = pd.concat(dataframes, ignore_index=True)

    st.success(f"✅ {len(uploaded_files)} arquivos unidos com sucesso!")
    st.dataframe(full_df.head(10))

    # Botão de download
    csv = full_df.to_csv(index=False)
    st.download_button(
        label="📥 Baixar CSV Final",
        data=csv,
        file_name="unificado.csv",
        mime="text/csv"
    )
else:
    st.info("📎 Faça upload de dois ou mais arquivos CSV para iniciar.")
