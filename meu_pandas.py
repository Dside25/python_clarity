import pandas as pd

# Criar um DATAFRAME com o pandas
data = {
    'Nome':['Caio', 'Guilherme', 'Carlos', ' Daniel'],
    'Idade':[25,30,35,40],
    'Salario':[5000,6000,7000,8000]    
}

df = pd.DataFrame(data)

# Exibindo o DataFrame
print('=Conteudo do Dataframe')
print(df)

# SELECIONANDO UMA COLUNA
print("\nColuna de nome:")
print(df['Nome'])

# FILTRANDO LINHAS (EX: IDADE MAIOR QUE 30)
print("\nPessoas com idade maior que 30:")
print(df[df['Idade']>30])

# ADICIONANDO UMA NOVA COLUNA

df["Imposto"] = df["Salario"] * 0.12
print("\nDataframe com a nova coluna de 'Imposto':")
print(df)

# CALCULANDO MEDIA DO SALARIO

mediaSalario = df['Salario'].mean()
print("\nMedia Salarial:")
print(mediaSalario)

somaSalario = df['Salario'].sum()
print("\nSoma Salarial:")
print(somaSalario)

# SALVANDO O DATAFRAME EM UM ARQUIVO CSV

df.to_csv('minha_tabela.csv', index=False)
print("\nArquivo Salvo com Sucesso:")
print("\nArquivo Salvo com Sucesso")