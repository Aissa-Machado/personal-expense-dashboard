import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from data_loader import carregar_dados
import matplotlib.dates as mdates

st.set_page_config(page_title="Painel de Gastos", layout="wide")

# Carregar dados
caminho_arquivo = "data/expenses-test.csv"
df = carregar_dados(caminho_arquivo)
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')

st.title("💰 Painel de Controle de Gastos Pessoais")

# Resumo geral
total_gastos = df['amount'].sum()
media_geral = df['amount'].mean()
st.markdown(f"**🔢 Total de gastos:** R$ {total_gastos:.2f}")
st.markdown(f"**📊 Média geral por compra:** R$ {media_geral:.2f}")

# Filtros interativos
st.sidebar.header("🔍 Filtros")
categorias = st.sidebar.multiselect("Filtrar por categoria:", options=df['category'].unique(), default=df['category'].unique())

data_min = df['date'].min()
data_max = df['date'].max()
data_range = st.sidebar.date_input("Filtrar por data:", [data_min, data_max])

# Aplicar filtros
df_filtrado = df[
    (df['category'].isin(categorias)) &
    (df['date'] >= pd.to_datetime(data_range[0])) &
    (df['date'] <= pd.to_datetime(data_range[1]))
]

# Gráficos
st.subheader("📊 Total por Categoria")
soma = df_filtrado.groupby('category')['amount'].sum()
st.dataframe(soma)

fig1, ax1 = plt.subplots()
ax1.pie(soma, labels=soma.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

st.subheader("📈 Média por Categoria")
media = df_filtrado.groupby('category')['amount'].median()
st.dataframe(media)

st.subheader("📌 Máximo por Categoria")
maximo = df_filtrado.groupby('category')['amount'].max()
st.dataframe(maximo)

st.subheader("📅 Média de Gastos por Mês")
media_mes = df_filtrado.groupby('month')['amount'].mean()
st.line_chart(media_mes)

st.subheader("📆 Total de Gastos por Mês")
gastos_por_mes = df_filtrado.groupby('month')['amount'].sum()
st.bar_chart(gastos_por_mes)

# Gráfico acumulativo de gastos ao longo do tempo
st.subheader("📈 Evolução Acumulativa dos Gastos")
df_filtrado_sorted = df_filtrado.sort_values('date')
df_filtrado_sorted['acumulado'] = df_filtrado_sorted['amount'].cumsum()
fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(df_filtrado_sorted['date'], df_filtrado_sorted['acumulado'], marker='o')
ax2.set_title("Total Acumulado ao Longo do Tempo")
ax2.set_xlabel("Data")
ax2.set_ylabel("R$ Acumulado")

# Formatação de datas no eixo X
ax2.xaxis.set_major_locator(mdates.AutoDateLocator())
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))  # Formato tipo: "Mai 15"
plt.xticks(rotation=45)  # Inclina as datas
plt.tight_layout()

st.pyplot(fig2)
# Insights extras
mes_mais_gasto = gastos_por_mes.idxmax()
valor_mais_gasto = gastos_por_mes.max()
st.markdown(f"💸 **Mês com maior gasto:** {mes_mais_gasto} – R$ {valor_mais_gasto:.2f}")

cat_mais_gasto = soma.idxmax()
valor_cat_mais_gasto = soma.max()
st.markdown(f"🏆 **Categoria com maior gasto:** {cat_mais_gasto} – R$ {valor_cat_mais_gasto:.2f}")

# Top 5 maiores compras
st.subheader("🔝 Top 5 Maiores Compras")
top5 = df_filtrado.sort_values(by='amount', ascending=False).head(5)
st.dataframe(top5[['date', 'description', 'category', 'amount']])

# Download CSV filtrado
st.sidebar.markdown("### 📥 Baixar dados filtrados")
csv = df_filtrado.to_csv(index=False).encode('utf-8')
st.sidebar.download_button("⬇️ Baixar CSV", data=csv, file_name="gastos_filtrados.csv", mime='text/csv')
