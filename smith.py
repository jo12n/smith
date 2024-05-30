import random
import numpy as np

filas = 8  # Número de filas de la matriz
columnas = 4  # Número de columnas de la matriz

# Crear matriz con números enteros aleatorios
matriz = np.array([[random.randint(-1,1) for j in range(columnas)] for i in range(filas)])
matriz = np.array([[1,0,0],[0,2,6],[0,4,2]])
# Mostrar la matriz
print(matriz)

def pivote2(matriz):
    if matriz[0][0] == 0:
        for fila in range(1,len(matriz)):
            for columna in range(1,len(matriz[fila])):
                if matriz[fila][columna]  != 0:
                    # Si algún elemento no es divisible, retorna False
                    matriz[[0,fila]] = matriz[[fila,0]]
                    matriz[:, [columna,0]] = matriz[:, [0, columna]]
                    break
            if matriz[0][0] != 0:
                break
        if matriz[0][0] == 0:
            return matriz, True
    return matriz, False

def pivote1(matriz):
    if matriz[0][0] == 0:
        matriz, matrizcero = pivote2(matriz)
    else:
        matrizcero = False
    if not matrizcero:
        for fila in range(1,len(matriz)):
            if abs(matriz[fila][0]) < abs(matriz[0][0]) and matriz[fila][0]!=0:
                # Si algún elemento no es divisible, retorna False
                matriz[[0,fila]] = matriz[[fila,0]]
        return matriz, False
    else:
        return matriz, True

def cerofila(matriz):
    matriz, matrizcero = pivote1(matriz)
    if matrizcero:
        return matriz
    else:
        while np.sum(matriz[:,0] != 0) > 1:
            for i in range(1,len(matriz)):
                matriz[i] = matriz[i]-(matriz[i][0]//matriz[0][0])*matriz[0]
                if matriz[i][0]%matriz[0][0] != 0:
                   matriz[[0,i]] = matriz[[i,0]] 
        return matriz,matrizcero
        
def divide_matriz(matriz):
    for fila in range(1,len(matriz)):
        for columna in range(1,len(matriz[fila])):
            if matriz[fila][columna]%matriz[0][0] != 0:
                    # Si algún elemento no es divisible, retorna False
                    matriz[[0,fila]] = matriz[[fila,0]]
                    matriz[:, [columna,0]] = matriz[:, [0, columna]]
                    break
            if matriz[0][0] != 0:
                break
        if matriz[0][0] == 0:
            return matriz, True
    return matriz, False

def smith1(matriz):
    matriz,matrizcero = cerofila(matriz)
    f= matriz[0][0]
    M,_ = cerofila(matriz.T)
    matriz = M.T
    while f != matriz[0][0]:
        f = matriz[0][0]
        matriz,_ = cerofila(matriz)
        M,_ = cerofila(matriz.T)
        matriz = M.T
    for i in range(1,len(matriz)):
        for j in range(1,len(matriz[0])):
            if matriz[i][j]%matriz[0][0] != 0:
                matriz[i] = matriz[i]+matriz[0]
                matriz[:,j] = matriz[:,j]-(matriz[i][j]//matriz[0][0])*matriz[:,0]
                matriz[[0,i]] = matriz[[i,0]]
                matriz[:, [j,0]] = matriz[:, [0, j]]
                smith1(matriz)
    return matriz,matrizcero

def smith(matriz):
    matriz_de_ceros = np.zeros((len(matriz), len(matriz[0])))
    m = min(len(matriz), len(matriz[0]))
    for i in range(m):
        matriz,matrizcero = smith1(matriz)
        if matrizcero:
            return matriz_de_ceros
        else:
            matriz_de_ceros[i,i] = matriz[0,0]
            matriz = matriz[1:,1:]
    return matriz_de_ceros



matriz = smith(matriz)
print('_____________')
print(matriz)