'''RETO 3: Realizar un algoritmo que permita insertar elementos en un diccionario. 
El docente debe ser capaz de ingresar la siguiente información por teclado:

-> Nombre del estudiante
-> Nombre de la asignatura
-> Nota del Laboratorio N°1
-> Nota del Laboratorio N°2

La ponderación del Laboratorio N°1 es de un 30% del promedio final y el 
Laboratorio N°2 pondera 70% de la nota final.

El algoritmo debe arrojar toda la información ingresada más el promedio 
final ponderado. Este promedio debe estar en un formato de punto flotante de máximo 1 decimal.'''

estudiante = input("Ingrese el nombre del estudiante: ")
asignatura = input("Ingrese el nombre de la asignatura: ")
nota1= float(input("Ingrese la nota del Laboratorio N°1: "))
nota2 = float(input("Ingrese la nota del Laboratorio N°2: "))

promedio = (nota1 * 0.3) + (nota2 * 0.7)

dic = {
    "nombre_estudiante": estudiante,
    "nombre_asignatura": asignatura,
    "nota_1": nota1,
    "nota_2": nota2,
    "promedio": round(promedio, 1) 
}

print(dic)
