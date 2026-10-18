import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Survey Insights Generator", layout="wide")

st.title("📊 Survey Insights Generator")
st.markdown("Upload your survey CSV to generate automatic insights and visualizations.")

# Widget de upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Carrega os dados
    df = pd.read_csv(uploaded_file)

    # 1. Visão Geral
    st.header("1. Data Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows (Participants)", df.shape[0])
    col2.metric("Total Columns (Questions)", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))

    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    # 2. Análise de Colunas
    st.header("2. Column Analysis")
    
    # Separa colunas numéricas e categóricas automaticamente
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns

    if len(numeric_cols) > 0:
        st.subheader("Numeric Columns Distribution")
        selected_num_col = st.selectbox("Select a numeric column to plot", numeric_cols)
        fig_hist = px.histogram(df, x=selected_num_col, nbins=20, title=f"Distribution of {selected_num_col}")
        st.plotly_chart(fig_hist, use_container_width=True)

    if len(categorical_cols) > 0:
        st.subheader("Categorical Columns Breakdown")
        selected_cat_col = st.selectbox("Select a categorical column to plot", categorical_cols)
        
        # Prepara os dados para o gráfico de barras
        val_counts = df[selected_cat_col].value_counts().reset_index()
        val_counts.columns = [selected_cat_col, 'Count']
        
        fig_bar = px.bar(val_counts, x=selected_cat_col, y='Count', title=f"Count of {selected_cat_col}")
        st.plotly_chart(fig_bar, use_container_width=True)

    # 3. Estatísticas Descritivas
    st.header("3. Descriptive Statistics")
    st.dataframe(df.describe())

else:
    st.info("👆 Please upload a CSV file to begin.")