###ESTE ES UN COMENTARIO
""" ESTE 
ES UN COMENTARIO 
MULTILINEA """

##GUIA RÁPIDA: CONOCIENDO LAS VARIABLES EN PYTHON - 05 DE ABRIL 2023

#Un simple print
print("Hola soy Constanza!")

#01-DECLARANDO VARIABLES
nombre = "Constanza"
name = "Victor"

#02-IMPRESION DE UNA VARIABLE
print(nombre)
print("Hola soy",nombre)

#Declarando una tercera variable de tipo númerico
edad = 29

#03-IMPRESION DE TEXTO + VARIABLE
print("Mi edad es de",edad)

#04-IMPRIMIENDO 2 VARIABLES EN UNA MISMA LINEA (concatenación)
#print("Hola mi nombre es" + nombre + "y tengo" + edad + "años") #Esta sentencia da error
print("Hola mi nombre es"+" " +name+" "+"y tengo"+" "+str(edad)+" "+"años")

##05-ACTUALIZANDO LA VARIABLE NOMBRE (Mutable)
nombre = "Diego"
print ("Hola mi nuevo nombre es", nombre)

#06-¿VARIABLES EN UNA SOLA LINEA?
ciudad, region, pais, year = "Puerto Montt", "Los Lagos", "Chile", 2010.
print("Yo naci en la ciudad de", ciudad,", region de",region,pais,", el año",int(year))

#07-UTILIZANDO LA INSTRUCCIÓN INPUT
nombre1 = input("¿Cuál es tu nombre?\n")
print("Tu nombre es:",nombre1)