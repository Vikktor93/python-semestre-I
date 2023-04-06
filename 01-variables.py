###ESTE ES UN COMENTARIO
""" ESTE ES UN COMENTARIO IGUAL """

##GUIA RÁPIDA: CONOCIENDO LAS VARIABLES EN PYTHON - 05 DE ABRIL 2023

#Un simple print
print("Hola soy Constanza!")

#Declarando dos variable
nombre = "Constanza"
name = "Victor"

#Impresion de una variable
print(nombre)
print("Hola soy",nombre)

#Declarando una tercera variable tipo númerico
edad = 29

#Impresion de la tercera variable
print("Mi edad es de",edad)

###Imprimiendo 2 variables en una misma sentencia (concatenación)
#print("Hola mi nombre es" + nombre + "y tengo" + edad + "años") #Esta sentencia da error
print("Hola mi nombre es"+" " +name+" "+"y tengo"+" "+str(edad)+" "+"años")

##Actualizando la variable nombre (Mutable)
nombre = "Diego"
print ("Hola mi nuevo nombre es", nombre)

#Utilizando la instrucción input
nombre1 = input("¿Cuál es tu nombre?\n")
print("Tu nombre es:",nombre1)