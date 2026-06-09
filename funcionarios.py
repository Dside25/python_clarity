import pandas as pd

# Dados dos funcionarios
dados = {
    "Nome":['Maria','Mariana','Camila','Jose','Daniel'],
    "Idade":[28, 42,31,24,36],
    "Cargo":['Analista','Gerente','Desenvolvedor','Estagiaria0','Analista'],
    "Salario":[5500, 9000, 7500, 2500, 6200]
}

# Criando o Dataframe

df = pd.DataFrame(dados)

#Exibindo o dataFrame completo:

print("=== Dataframe Completo ===")
print(df)

#Exibir apenas a coluna Cargo

print("\nColuna de Cargo:")
print(df['Cargo'])

# Exibir apenas funcionarios com salario maior que 6000

print("\nPessoas com idade maior que 30:")
print(df[df['Salario']>6000])

# Funcionarios com idade maior que 35

print("\nPessoas com idade maior que 30:")
print(df[df['Idade']>35])

# Criar uma coluna de bonus de 15%

df["BONUS"] = df["Salario"] * 0.15
print("\nDataframe com a nova coluna de 'BONUS 15%':")
print(df)

# Criar uma coluna de salario final (Salario+Bonus)

df["Salario+BONUS"] = df["Salario"] + df["Salario"] * 0.15
print("\nDataframe com a nova coluna de 'SALARIO+BONUS':")
print(df)

# Estatisticas

print('\n=== "Estatisticas" ===')
print(f"Media Salarial: R$ {df['Salario'].mean():.2f}")
print(f"Maior Salario: R${df['Salario'].max():.2f}") 
print(f"Menor Salario: R${df['Salario'].min():.2f}")

# Ordenado por salario

print('\n=== Funcionarios ordenados por salario ===')
print(df.sort_values(by='Salario', ascending=False))

# Quantidade por Cargo

print('\n=== "Quantidade por Cargo" ===')
print(df["Cargo"].value_counts())

# Funcionarios cujo o nome começa com M

print("\n=== Funcionarios com nome iniciando em 'M' ===")
print(df[df['Nome'].str.startswith("M")])

# Funcionarios com maior salario final

maiorSalarioFinal = df.loc[df['Salario+BONUS'].idxmax()]
print('\n=== "Funcionarios com Maior Salario Final" ===')
print(maiorSalarioFinal)

# Salvando em CSV

df.to_csv("Funcionarios.csv", index=False)
print('\n=== Arquivo "funcionarios.csv" salvo com sucesso. ===')
print()