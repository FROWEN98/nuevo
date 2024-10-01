#Buscamos un elemento de nuestro array
list = [
    [1,6,8,7,8,10,14],
    [2,8,6,7,9,1,10]
    ]   # Declaramos la lista

print(list) #Imprimimos la lista
def buscar(n,l):    #Creamos una función
    for i in range(len(list)):  #Recorremos filas
        for j in range(len(list)): #Recorremos las columnas
          if list[i] [j] == n :
            return i,j  #Retornamos los inidec

    return "No encontramos"
numero = int(input("Que numero desea buscar: "))
print(list) #Imprimimos la lista
print(f"El numero {numero} esta en la posición ",buscar(numero,list))   #Imprimimos


#Ordenamos una posición
def bubble_sort(fila):
    # Algoritmo de ordenación Bubble Sort
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]




def orden(listas, fila):
    # Ordena la fila especificada de la matriz
    if 0 <= fila < len(listas):
        bubble_sort(listas[fila])
    else:
        print("Índice de fila esta fuera de rango.")




# Definición de la matriz
listas = [
    [14,15,2,6,17,3,6,8],
    [10,2,5,6,3,1,11,4,5],
    [10,9,8,7,6,5,4,3,2,1]
]
# Imprimir matriz original

print("\n\nMatriz original:")
for filas in listas:
    print(filas)

# Ordenar la segunda fila indice 1
orden(listas,2)

# Imprimimimos  la lista  después de ordenar
print("\nMatriz después de ordenar la fila :")
for filas in listas:
    print(filas)




