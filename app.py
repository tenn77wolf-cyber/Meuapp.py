import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Meu App Streamlit", layout="wide")
st.title(" Meu App Streamlit")

with st.sidebar:
    selected = option_menu(
        menu_title=" Menu Principal",
        options=["Início", "Dashboard", "Contato", "Sobre"],
        icons=["house", "bar-chart", "envelope", "info-circle"],
        default_index=0
    )

def pagina_inicio():
    st.header(" Bem-vindo!")
    st.success("Você está na página inicial do aplicativo.")
    st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085", use_column_width=True, caption="Tecnologia & Simplicidade")

    st.subheader(" Preencha o formulário:")
    with st.form("formulario_usuario"):
        nome = st.text_input("Digite seu nome")
        idade = st.slider("Selecione sua idade", 0, 100, 25)
        feedback = st.text_area("O que achou do app?", "")
        enviado = st.form_submit_button("Enviar")

        if enviado:
            st.success(f"Obrigado, {nome}! Seu feedback foi enviado com sucesso.")

def pagina_dashboard():
    st.header(" Dashboard de Dados")
    
    uploaded_file = st.file_uploader("Faça upload de um arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Arquivo carregado com sucesso!")
        st.subheader("🔍 Visualização dos Dados:")
        st.dataframe(df)

        st.subheader(" Gráfico de Barras")
        numeric_columns = df.select_dtypes(include=["int", "float"]).columns.tolist()

        if len(numeric_columns) >= 2:
            col_x = st.selectbox("Coluna para Eixo X", options=numeric_columns)
            col_y = st.selectbox("Coluna para Eixo Y", options=numeric_columns, index=1)

            fig, ax = plt.subplots()
            ax.bar(df[col_x], df[col_y], color='teal')
            ax.set_xlabel(col_x)
            ax.set_ylabel(col_y)
            ax.set_title(f"{col_y} por {col_x}")
            st.pyplot(fig)
        else:
            st.warning("O CSV precisa ter pelo menos duas colunas numéricas para gerar o gráfico.")

def pagina_contato():
    st.header(" Contato")
    with st.form("form_contato"):
        nome = st.text_input("Marcos Paulo Alves Borges")
        email = st.text_input("marcos2@gmail.com")
        mensagem = st.text_area("Isso e um teste")
        enviado = st.form_submit_button("Enviar")

        if enviado:
            st.success(f"Obrigado, {nome}! Entraremos em contato pelo e-mail: {email}")

    st.subheader(" Redes Sociais")
    st.markdown("""
        -  E-mail: marcos@email.com  
        -  Site: [Seu Site](https://seusite.com)  
        -  [LinkedIn](https://www.linkedin.com)
    """)

def pagina_sobre():
    st.header("ℹ Sobre o Projeto")
    st.info("Este é um aplicativo criado com Streamlit como exemplo para aprendizado.")

    st.markdown("""
        ###  Desenvolvedor:
        **Marcos Paulo Alves Borges**

         [LinkedIn](https://www.linkedin.com)  
         [Seu Site Pessoal](https://seusite.com)  
         marcos@email.com
    """)

    st.subheader(" Tecnologias Utilizadas:")
    st.markdown("""
    - [Streamlit](https://streamlit.io/)
    - [Python](https://www.python.org/)
    - [Pandas](https://pandas.pydata.org/)
    - [Matplotlib](https://matplotlib.org/)
    """)

if selected == "Início":
    pagina_inicio()
elif selected == "Dashboard":
    pagina_dashboard()
elif selected == "Contato":
    pagina_contato()
elif selected == "Sobre":
    pagina_sobre()
