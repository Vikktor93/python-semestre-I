###ESTE ES UN COMENTARIO
""" ESTE ES UN COMENTARIO IGUAL """

##GUIA RÁPIDA: CONOCIENDO LAS VARIABLES EN PYTHON - 05 DE ABRIL 2023

#Un simple print
print("Hola soy Constanza!")

#Declarando una variable
nombre = "Constanza"

#Impresion de una variable
print("Hola soy",nombre)

#Declarando una segunda variable
edad = 20

#Impresion de la segunda variable
print("Mi edad es de",edad)

###Imprimiendo 2 variables en una misma sentencia (concatenación)
#print("Hola mi nombre es" + nombre + "y tengo" + edad + "años")
print("Hola mi nombre es" + nombre + "y tengo" + str(edad) + "años")

##Actualizando la variable nombre (Mutable)
nombre = "Diego"
print ("Hola mi nombre es", nombre)

#Utilizando la instrucción input
nombre = input("¿Cuál es tu nombre?\n")
print("Tu nombres es:",nombre)