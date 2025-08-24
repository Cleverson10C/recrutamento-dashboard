import pandas as pd
import streamlit as st
# Carregar dados dos candidatos a partir de uma planilha Excel
candidatos = pd.read_excel('candidatos.xlsx')

# Exportar para Excel
candidatos.to_excel('candidatos.xlsx', index=False)

st.set_page_config(page_title="Dashboard de Candidatos", layout="wide")
st.title("Dashboard de Candidatos")

# Filtros
cidade = st.sidebar.multiselect('Filtrar por cidade', candidatos['cidade'].unique())
profissao = st.sidebar.multiselect('Filtrar por profissao', candidatos['profissao'].unique())

df_filtrado = candidatos.copy()
if cidade:
	df_filtrado = df_filtrado[df_filtrado['cidade'].isin(cidade)]
if profissao:
	df_filtrado = df_filtrado[df_filtrado['profissao'].isin(profissao)]

# Visualização de quantidades
col1, col2 = st.columns(2)
with col1:
	st.subheader('candidatos por cidade')
	st.bar_chart(df_filtrado['cidade'].value_counts())
with col2:
	st.subheader('candidatos por profissao')
	st.bar_chart(df_filtrado['profissao'].value_counts())

# Listagem dos candidatos
st.subheader('Lista de Candidatos')
def format_link(url, texto):
	return f"[{texto}]({url})"

df_exibir = df_filtrado.copy()
df_exibir['carteira digital'] = df_exibir.apply(lambda x: format_link(x['carteira digital'], 'Carteira'), axis=1)
df_exibir['curriculo'] = df_exibir.apply(lambda x: format_link(x['curriculo'], 'Curriculo'), axis=1)

st.dataframe(df_exibir[['nome', 'cidade', 'profissao', 'curriculo', 'carteira digital']], use_container_width=True)

# Exportação de lista filtrada
st.download_button(
	label="Exportar lista filtrada (CSV)",
	data=df_filtrado.to_csv(index=False).encode('utf-8'),
	file_name='candidatos_filtrados.csv',
	mime='text/csv'
)
