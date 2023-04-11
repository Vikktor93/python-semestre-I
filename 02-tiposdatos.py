###GUIA RÁPIDA TIPOS DE DATOS EN PYTHON

#01-DATOS DE TIPO NÚMERICO
edad = 29 #entero
estatura = 1.71 #real
peso = 70.5 #real
complejo =  1 + 4j #complejo

print("01-DATOS NÚMERICOS");
print("Mi estatura es de",estatura,"m","y mi peso de",peso,"kg")
print("Impresion de un número complejo:",complejo,"\n")

#Transformando un real a entero
print("Transformando un valor real a entero:",int(peso))

#Transformando un entero a real
print("Transformando un valor entero a real:",float(edad))

#OPERACION ARITMETICA BÁSICA
imc = peso/estatura**2
print("Mi IMC es de:",imc,"\n")

print("Mi IMC es de: {:.2f}".format(imc),"\n")

#02-DATOS DE TIPO CADENA DE CARACTERES 
asignatura = "Programación"
carrera = "Ingenieria Civil en Informática"
print("02-STRINGS")
print("La asignatura de",asignatura,"corresponde a la carrera de",carrera)

#Utilizando la función len (cuenta la cantidad de caracteres)
print("La cantidad de caracteres de la palabra", asignatura, "es de:",len(asignatura))
print("La cantidad de caracteres de la palabra", carrera, "es de:",len(carrera),"\n")


#03-VALORES BOOLEANOS
ampolleta = False
interruptor = True

#Con type sabemos el tipo de datos que estamos tratando
print("03-BOOLEANS")
print(ampolleta,interruptor)
print("La variable ampolleta es de tipo:",type(interruptor),"\n")

#04-DATOS TIPO ARRAY/LIST (Objetos de Tipo Colección) - Mutabilidad
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastián"]
num = [1,2,3,4,5,6]
lenguaje = ["Python"]
data = ['Osorno', {'UV': 'nivel bajo', 'Temp °C': 15}, (-40.5725, -73.1353)]
print("04-ARREGLOS/LISTAS")
print("Arreglo de cadena de caracteres:",estudiantes)
print("Arreglo de números:",num)
print("Arreglo de un elemento:",lenguaje)
print("Esto igual es un arreglo o lista:",data)

lenguaje = ["JavaScript"]
print("Nuevo valor del Arreglo de un elemento:",lenguaje)

#Reasignando el valor del primer elemento de la lista
estudiantes[0] = "Gabriela"
print("El arreglo de estudiantes es:",estudiantes)

#¿Qué hace estas funciones?
print(list("Python"))
print(list(range(10)))
print("\n")


#05 - TUPLAS - No mutables
grupo1 = ("Matias","Cristian","Felipe")
print("05-TUPLAS")
print(type(grupo1))
print("\n")

#Reasignando el primer elemento de la tupla
#grupo1[0] = "Constanza"
#print(grupo1)


#06 - SETS (Conjuntos) - Estructura fija
#Formas de inicializar un Set
conjunto_colores = set({"Azul","Rojo","Verde"}) #utilizando la funcion set
conjunto_animales = {"Gato","Perro","Loro"}     #utilizando corchetes

print("06-SETS")
print(type(conjunto_colores)) #tipo de dato set
print(type(conjunto_animales)) #tipo de dato set
print("El primer set contiene los siguientes colores:",conjunto_colores)
print("El segundo set contiene los siguientes animales:",conjunto_animales)

#print(conjunto[0]) #accediendo al primer elemento del set
conjunto_colores.add("Celeste")
print("El set de colores lo conforman:",conjunto_colores) #un set es una estructura desordenada a diferencia de una Lista

conjunto_animales.add("Gato")
print("El set de animales lo conforman:",conjunto_animales,"\n") #un set no acepta duplicados, a diferencia de las listas que si.


#07 - DICCIONARIOS


#08-¿Forzando el tipo de dato?
universidad: str = "Universidad de Los Lagos"
universidad = 90
universidad = True

#¿Al final que tipo de dato es la variable universidad?




