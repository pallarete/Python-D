''' METODOS DE CADENAS '''
import os
os.system('cls')

cadena1 = 'Hola,Soy,Alex'
cadena2 = 'Bienvenido monstruo'

#Pasar a minusculas
resultado = cadena1.lower()

#Pasar la primera letra a mayusculas
primer_letra = cadena1.capitalize()

#Encontrar el indice de una letra.Si no encuentra devuelve -1
encontrada = cadena1.find('S')

#Encontrar el indice de una letra.Si no devuelve una excepcion
encontrada = cadena1.index('S')

#Si es numerico devulve true
numerico = cadena1.isnumeric()

#Si es alfanumerico devuelve booleano
cadena3 ='holacaracola'
es_alfanumerico = cadena3.isalpha()

#nos dice el numero de ocurrencias en una cadena de una cadena pasada
coincidencias = cadena3.count('a')

#nos dice el numero de caracteres de una cadena
conteo = len(cadena1)

#verificar si una cadena empieza con el dato pasado
empieza_con = cadena1.startswith('Hola')

#verificar si una cadena termina con el dato pasado
termina_con = cadena1.endswith('Alex')

#reeemplaza lo que le pasemos como parametro a encontrar y si esta lo cambia por el dato pasado
cadena_nueva = cadena1.replace('la','lu')

#Separa cadenas donde encuentre el dato que le pasemos si existe en la cadena original
cadena_separada = cadena1.split(",")

print(resultado)
print(primer_letra)
print(encontrada)
print(numerico)
print(es_alfanumerico)
print(coincidencias)
print(conteo)
print(empieza_con)
print(termina_con)
print(cadena_nueva)
print(cadena_separada)
print(type(cadena_separada))

 




