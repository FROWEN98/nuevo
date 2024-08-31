#Buscamos un elemento de nuestro array
list = [
    [1,6,8,7,8,10,14],
    [2,8,6,7,9,1,10]
    ]   # Declaramos la lista

def buscar(n,l):    #Creamos una función
    for i in range(len(list)):  #Recorremos filas
        for j in range(len(list)): #Recorremos las columnas
          if list[i] [j] == n :
            return i,j  #Retornamos los inidec

    return "No encontramos"

print(list) #Imprimimos la lista
print("El numero esta en la posición ",buscar(1,list))   #Imprimimos


#Ordenamos una posición

lista = [
    [1, 6, 8, 7, 8, 10, 14],
    [2, 8, 6, 7, 9, 1, 10]
]

# Aplanamos la lista en una lista unidimensional
listas = [elemento for fila in list for elemento in fila]

# Ordenamos la lista en orden ascendente
listas.sort()



# Imprimimos el resultado
print("Lista  ordenada:", listas)

