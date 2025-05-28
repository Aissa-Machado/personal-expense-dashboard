import pandas as pd

COLUNAS_PADRAO = {
    "Data": "date",
    "Categoria": "category",
    "Valor": "amount",
    "Descrição": "description",
    "Forma de Pagamento": "payment_method"
}

def carregar_dados(file):
    df = pd.read_csv(file)
    df = df.rename(columns=lambda col: COLUNAS_PADRAO.get(col, col))
    return df
