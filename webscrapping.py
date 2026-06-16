import requests
import pandas as pd
import sqlite3
import datetime
import time
import random

from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36'}

baseURL = "https://www.sampaingressos.com.br/templates/ajax/lista_espetaculo.php"

filmes = []

data_hoje = datetime.date.today().strftime("%d-%m-%Y")
agora = datetime.datetime.now()

bancoDados = r"C:\Users\noturno\Desktop\Phyton_Daniel_Noite\banco_filmes.db" 
saidaCsv = f"C:/Users/noturno/Desktop/Phyton_Daniel_Noite/show_sampaingressos_{data_hoje}.csv"

paginaLimite = 1
pagTempoMin = 1
pagTempoMax = 5
cardTempMin = 1
cardTempMax = 1


for pagina in range(1, paginaLimite + 1):
    url = f"{baseURL}?pagina={pagina}&tipoEspetaculo=shows"
    print(f"Coletando Dados da página {pagina} : {url}")
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, "html.parser")
    
    if resposta.status_code != 200:
        print(f"Erro ao carregar a pagina {pagina}. Código de erro é: {resposta.status_code}")
        continue
    
    cards = soup.find_all("div", id="box_espetaculo")
    
    for card in cards:
        try:
            titulo_tag = card.find("b", class_="titulo")
            local_tag = card.find("Span", class_="local")
            horario_tag = card.find("Span", class_="horario")
            
            titulo = titulo_tag.text.strip()if titulo_tag else "N/A"
            local = local_tag.text.strip() if local_tag else "N/A"
            horario = horario_tag.text.strip() if horario_tag else "N/A"
            
            if titulo != "N/A":
                filmes.append({
                    "Titulo" : titulo,
                    "Local" : local,
                    "Horario" : horario
                })
            else:
                print("Cartão sem Titulo(Ignorado)")    
                
            tempo = random.uniform(cardTempMin, cardTempMax)
                
            time.sleep(tempo)    
            
            
        except Exception as e:
            print(f"Erro ao processar o cartão. Erro: {e}")
    
    tempo = random.uniform(cardTempMin, cardTempMax)
    time.sleep(tempo)        

df = pd.DataFrame(filmes)    
print(df.head())


df.to_csv(saidaCsv, index=False, encoding="utf-8-sig", quotechar="'", quoting=1)

conn = sqlite3.connect(bancoDados)
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS shows(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo TEXT,
            Local  TEXT,
            Horario TEXT
        )       
''')

for evento in filmes:
    try:
        cursor.execute('''
                       INSERT INTO shows (Titulo, Local, Horario) VALUES (?,?,?)
                       
                       
                       
                       ''',(
                           evento['Titulo'],
                           evento['Local'],
                           evento['Horario']
                       ))
        
        
    except Exception as e:
        print(f'Erro ao inserir o evento{evento['Titulo']} no banco de dados. Codigo de identificação do erro: {e}')

conn.commit()
conn.close()

print('-------------------------------------')
print('Dados raspados com sucesso!')
print('Obrigado por usar meu BOT')
print('Feito com ♥ por D.Side')
    


