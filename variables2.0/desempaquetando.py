''' Desempaquetando los datos de tuplas'''
import os
os.system('cls')

#Creando una tupla
datos_en_tupla =('Alex','Vazquez', 10000)
datos_en_lista =['Alex','Vazquez', 10000]
datos_en_conjunto ={'Alex','Vazquez', 10000}

# el numero de variables tiene que coincidir con la cantidad de elementos de la tupla
nombre, apellido, subscriptores = datos_en_conjunto

# se pueden imprimir varias variables en un print
# Los conjuntos no mantienen un orden
print(nombre,apellido,subscriptores)
print(apellido)
print(subscriptores)