import sqlite3

# Criar o banco de dados (ou criar se caso não existir)

def conectarBanco() :
    conexao = sqlite3.connect('meu_banco.db')
    return conexao

# CRIANDO UMA TABELA NESSE BANCO DE DADOS 

def criarTabela() :

    conexao = conectarBanco()
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
        )
    ''')
    
    conexao.commit()
    conexao.close()
    
def inserirUsuarios(nome, idade) :

    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES (?, ?)
                    
    ''', (nome, idade))
            
    conexao.commit() 
    conexao.close()
    
def listarUsuarios() :
        
        conexao = conectarBanco()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall
            
        for usuario in usuarios :
            print(usuarios)
        conexao.close()
        
criarTabela()

inserirUsuarios("Caio",39)
inserirUsuarios("Leandro", 39)
inserirUsuarios("Carlos", 58)                
inserirUsuarios("Guilherme", 25 )                           
inserirUsuarios("Daniel", 32)
inserirUsuarios("Vinicius", 22)    

listarUsuarios()