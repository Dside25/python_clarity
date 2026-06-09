import numpy as np

arr = np.array([1,2,3,4,5])

print("ARRAY NUMPY:")
print(arr)

#Operações matematicas com array

print('\n Array multiplicado por 2')
print('arr * 2')

# Operações entre Arrays

arr2 = np.array([6, 7, 8, 9, 10])
print('\nSomando duas Arrays:')
print(arr + arr2)

# Criando uma Matriz

matriz = np.array(
    [
        [1,2,3,],
        [4,5,6]
    ]
)
print('\nMatriz 2x3')
print(matriz)

# Soma de uma matriz

print('\nSoma:')
print(np.sum(matriz))

# Media da matriz

print('n\Media:')
print(np.mean(matriz))

# Transposta da matriz

print('\nMatriz Transposta:')
print(matriz.T)

# Gerando numeros Aleatorios

print('\nNumeros aleatorios entre 0 e 1:')
print(np.random.rand(3,3))