#ESTE UN COMENTARIO DE UNA LINEA
""" ESTE 
ES UN COMENTARIO 
MULTILINEA """

##GUIA RÁPIDA: CONOCIENDO LAS VARIABLES EN PYTHON - 10 DE ABRIL 2023

#Un simple print
print("Hola soy Constanza!")

#01-DECLARANDO VARIABLES DE TIPO CADENA DE TEXTO
nombre = "Constanza"
name = "Victor"

#02-IMPRESION DE UNA VARIABLE
print(name)
print("Hola soy",name)

#Declarando una tercera variable de tipo númerico
edad = 29

#03-IMPRESION DE TEXTO + VARIABLE (IMPRESIÓN VARIABLE EDAD)
print("Mi edad es de", edad)


#04-IMPRIMIENDO 2 VARIABLES EN UNA MISMA LINEA 
#(concatenación con signo +, utilizando comas y Formato cadenas literales)
#print("Hola mi nombre es" + nombre + "y tengo" + edad + "años") #Esta sentencia da error ¿por qué?

print("Hola mi nombre es",nombre,"y tengo",edad) #Impresion separando con comas
print("Hola mi nombre es"+" "+name+" "+"y tengo"+str(edad)) #Concatenación con signo +
print(f"Hola mi nombre es {nombre} y tengo {edad} años") #Formato de cadenas literales (f-string)

##05-ACTUALIZANDO LA VARIABLE NOMBRE (Mutabilidad)
nombre = "Diego"
name = "Benjamin"
print ("Hola mi nuevo nombre es", nombre)
print ("Hola mi nuevo nombre es", name)


#06-¿VARIABLES EN UNA SOLA LINEA? (No es muy recomendable, solo en ciertas situaciones)
ciudad, region, pais, year = "Puerto Montt", "Los Lagos", "Chile", 2010.
print("Yo naci en la ciudad de", ciudad,", region de",region,pais,", el año",int(year))

#07-UTILIZANDO LA INSTRUCCIÓN INPUT
nombre1 = input("¿Cuál es tu nombre?\n")
edad1 = input("¿Cual es tu edad?\n")

print("Tu nombre es:",nombre1,"y tu edad es", edad1)