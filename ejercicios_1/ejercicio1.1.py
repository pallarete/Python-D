''' Ejercicio 1.1'''
import os
os.system('cls')

#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4 
curso_dalto = 1.5

#Duracion de crudo
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duracion

diferencia_con_min = 100 - curso_dalto / otros_cursos_min * 100
diferencia_con_max = 100 - curso_dalto *1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - curso_dalto / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_removido = 100 - otros_cursos_promedio *1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - curso_dalto *1000 // crudo_dalto / 10

print( f'El curso de Dalto dura un {diferencia_con_min}% menos que el más rapido')
print( f'El curso de Dalto dura un {diferencia_con_max}% menos que el más lento')
print( f'El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio')

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_removido}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')

#Mostrando diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 //curso_dalto / 10}')