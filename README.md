# 💰 Painel de Controle de Gastos Pessoais

Este projeto é uma aplicação interativa desenvolvida com **Python**, **Streamlit**, **Pandas** e **Matplotlib** para visualizar e analisar seus gastos mensais de forma prática e intuitiva.

---

## ✅ Funcionalidades

- 📊 **Total de gastos por categoria**
- 📈 **Média e máximo por categoria**
- 📅 **Total e média por mês**
- 📉 **Gráfico acumulativo de gastos**
- 🏆 **Mês e categoria com maior gasto**
- 🔝 **Top 5 maiores compras**
- 🔍 **Filtros interativos por categoria e data**
- 📥 **Download de CSV com dados filtrados**

---

## 🧪 Tecnologias usadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Streamlit](https://streamlit.io/)

---

## 📁 Estrutura do Projeto

painel_gastos/
├── app/
│ ├── main.py # Código principal do painel
│ ├── data_loader.py # Função de leitura dos dados
├── data/
│ └── expenses-test.csv # Exemplo de base de gastos
├── requirements.txt # Bibliotecas necessárias
└── README.md # Este arquivo

---

## 🚀 Como executar localmente

1. Clone este repositório:

git clone https://github.com/seu-usuario/painel-gastos.git

cd painel-gastos

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

Instale as dependências:

pip install -r requirements.txt

Execute o app:

streamlit run app/main.py

📋 Formato esperado do arquivo CSV

O arquivo deve conter as seguintes colunas:

[modelo_planilha_gastos_profissional (1).xlsx](https://github.com/user-attachments/files/20488274/modelo_planilha_gastos_profissional.1.xlsx)

[expense_template_en_profissional (1).xlsx](https://github.com/user-attachments/files/20488281/expense_template_en_profissional.1.xlsx)

| date       | description    | category    | amount |
| ---------- | -------------- | ----------- | ------ |
| 2025-05-01 | Supermercado X | Alimentação | 120.50 |
| 2025-05-02 | Uber corrida   | Transporte  | 35.00  |
| 2025-05-03 | Netflix        | Lazer       | 39.90  |


📌 Dica: Você pode editar seu próprio arquivo .csv com Excel, Google Sheets ou diretamente no VSCode.

🎯 Objetivo do Projeto

Este projeto foi desenvolvido com fins educativos e práticos, ajudando pessoas a terem mais clareza financeira, visualizando seus gastos de forma clara e acessível.

👩‍💻 Autora

Aissa Machado

🔗 https://www.linkedin.com/in/aissa-machado-a601b8168/

🐙 GitHub

📄 Licença
Este projeto está licenciado sob a MIT License.
