import pandas as pd
import numpy as np

# ========================
# CARREGAR COLUNAS
# ========================

df = pd.read_csv('drinks.csv')

# ========================
# RENOMEAR COLUNAS
# ========================

df.columns = [
    
    "Pais",
    "Cerveja",
    "Destilados",
    "Vinho",
    "LitrosAlcool"    
]

# ========================
# VISUALIZAÇÃO INICIAL
# ========================

print("=== PRIMEIRAS 5 LINHAS ===")
print(df.head())

print("\n === INFORMAÇÕES DO DATAFRAME ===")
print(df.info())

print("\n === ESTATISTICAS GERAIS ===")
print(df.describe())


# ========================
# ESTATISTICAS COM NUMPY
# ========================

print(f"Media: {np.mean(df['Cerveja']):.2f}")
print(f"Median: {np.median(df['Cerveja']):.2f}")
print(f"Maior Consumo: {np.max(df['Cerveja']):.2f}")
print(f"Menor Consumo: {np.min(df['Cerveja']):.2f}")
print(f"Desvio Padrão: {np.std(df['Cerveja']):.2f}")

# ========================
# TOP 10 CERVEJA
# ========================

print("\n === TOP 10 PAISES QUE MAIS CONSUMEM CERVEJA ===")

top10 = df.nlargest(10, "Cerveja")

print(top10[
    ["Pais","Cerveja"]
]
)

# ========================
# TOP 10 VINHO
# ========================

print("\n === TOP 10 PAISES QUE MAIS CONSUMEM VINHO ===")

top10 = df.nlargest(10, "Vinho")

print(top10[
    ["Pais","Vinho"]
    ]
)

# ========================
# FILTROS
# ========================

mediaAlcool = df['LitrosAlcool'].mean()
print("\n === ACIMA DA MEDIA DE ALCOOL ===")
print(
    df[df["LitrosAlcool"] > mediaAlcool][["Pais","LitrosAlcool"]]
)

# ========================
# NOVA COLUNA TOTAL
# ========================

df["TotalBebidas"] = (
    df["Cerveja"] + df["Destilados"] + df["Vinho"]
)

print("\n=== TOTAL DE BEBIDAS ===")
print(df[["Pais", "TotalBebidas"]].head())

# ========================
# Classificação com o NUMPEY
# ========================

condicoes = [
    df["LitrosAlcool"] <2,
    df["LitrosAlcool"] <5,
    df["LitrosAlcool"] <8,
    df["LitrosAlcool"] >=8,     
]

categorias = [
    
    "Muito Baixo",
    "Baixo",
    "Medio",
    "Alto"
]

df["NivelConsumo"] = np.select(
    condicoes,
    categorias,
    default = "Não Informado"
)

print("\n=== Classificao de Consumo ===")

print(
    df[
        ["Pais", "LitrosAlcool", "NivelConsumo"]
    ].head(20)
    
    
)

# ========================
# Classificação com o NUMPEY
# ========================

print("\n=== Quantidade de Pais Por Nivel ===")
print(df["NivelConsumo"].value_counts())

# ========================
# PAIS COM MAIOR CONSUMO TOTAL
# ========================

maiorConsumo = df.loc[df["TotalBebidas"].idxmax()]
print("\n=== MAIOR CONSUMO ===")
print(maiorConsumo)

# ========================
# ACIMA DA MEDIA EM TUDO
# ========================

mediaCerveja = df["Cerveja"].mean()
mediaDestilados = df["Destilados"].mean()
mediaVinho = df["Vinho"].mean()
print("\n=== ACIMA DA MEDIA EM TODAS AS BEBIDAS ===")
resultado = df[
    (df["Cerveja"] > mediaCerveja) &
    (df["Destilados"] > mediaDestilados) &
    (df["Vinho"] > mediaVinho) 
]

print(
    resultado[["Pais", "Cerveja", "Destilados", "Vinho"]]
)
# ========================
# CORRELAÇÃO
# ========================

print("\n=== MAIOR CORRELAÇÃO ===")

print(
    df[
        [
            "Cerveja",
            "Destilados",
            "Vinho",
            "LitrosAlcool"
        ]
    ].corr()
)

# ========================
# ORDENAÇÃO
# ========================

print("\n=== TOP 20 CONSUMO TOTAL ===")

print(
    df.sort_values(by="TotalBebidas", ascending=False)[["Pais", "TotalBebidas"]].head(20)
)

# ========================
# SALVAR CSV
# ========================

df.to_csv("drinks_processados.csv", index=False)