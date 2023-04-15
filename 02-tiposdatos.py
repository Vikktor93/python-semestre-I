#GUIA RÁPIDA TIPOS DE DATOS EN PYTHON
# Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

#01-DATOS DE TIPO NÚMERICO
edad = 29 #entero
estatura = 1.71 #real
peso = 70.5 
complejo =  1 + 4j #complejo

print("######## 01-DATOS NÚMERICOS ########");
print(f"Mi estatura es de {estatura} y mi peso es de {peso}")
print("Impresion de un número complejo:",complejo,"\n")

#Transformando un real a entero
print("Transformando un valor real a entero:",int(peso))

#Transformando un entero a real
print("Transformando un valor entero a real:",float(edad))

#OPERACION ARITMETICA BÁSICA
imc = peso / (estatura**2)
print("Mi IMC es de:",imc,"\n")

print("Mi IMC es de: {:.2f}".format(imc),"\n") #formateando el valor de salida a solo 2 decimales

#02-DATOS DE TIPO CADENA DE CARACTERES 
asignatura = "Programación"
carrera = "Ingenieria Civil en Informática"
print("######## 02-STRINGS ########")
print("La asignatura de",asignatura,"corresponde a la carrera de",carrera)

#Utilizando la función len (cuenta la cantidad de caracteres)
print("La cantidad de caracteres de la palabra", asignatura, "es de:",len(asignatura))
print("La cantidad de caracteres de la palabra", carrera, "es de:",len(carrera),"\n")

#03-VALORES BOOLEANOS
ampolleta = False
interruptor = True

print("######## 03-BOOLEANS ########")
print(ampolleta,interruptor)
print("La variable ampolleta es de tipo:",type(interruptor),"\n") #Con type sabemos el tipo de datos con el cual estamos trabajando

#Podemos cualquier valor y transformarlo a un Booleano
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("True"))
print(bool(1))
print("\n")

#04-DATOS TIPO LIST (Objetos de Tipo Colección) - (Mutables)
print("######## 04-LISTAS ########")

#Declarando e inicializando listas
nueva_lista = list()
otra_lista = []
print("Esta es una lista vacia:",nueva_lista)
print("Esta es otra lista vacia:",otra_lista)
print(type(otra_lista))

#Declarando tres listas diferentes listas
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastián", "Marco"]
num = [1,2,3,4,5,6]
lenguaje = ["Python"]


# ¿Se puede realizar una lista de datos compuestos?
data = ['Osorno', {'UV': 'nivel bajo', 'Temp °C': 15}, (-40.5725, -73.1353)]

print("Lista de cadena de caracteres:",estudiantes)
print("Lista de números:",num)
print("Lista de un elemento:",lenguaje)
print("Esto igual es una lista:",data)
print(len(lenguaje)) #para saber la cantidad de elementos de una lista
print(estudiantes.count("Marco")) #cantidad de ocurrencias de un elemento en especifico dentro de la lista

lenguaje = ["JavaScript"]
print("Nuevo valor del Arreglo de un elemento:",lenguaje)

#¿Como accedo a un elemento especifico de la lista?
print(estudiantes[0]) #correcto (primer elemento de la lista)
print(estudiantes[1]) #segundo elemento de la lista
#print(estudiantes[5]) #incorrecto
print("Posicion -2",estudiantes[-2]) #impresión desde atras hacia adelante


#Reasignando el valor de la posición 3 de la lista
estudiantes[3] = "Gabriela"
print("El nuevo arreglo de estudiantes es:",estudiantes)

#Inicializando otra lista de datos mixtos
data_asig = [10023,"Programación",1,True]

#¿Que hace este código?                                                                       #Desempaquetando elementos de la lista a variables
cod,ramo,semestre,estado = data_asig
print(ramo)

#¿Se pueden sumar listas?
print("Suma de listas",estudiantes + num)

#¿Qué operaciones hacen estas funciones?
print(list("Python"))
print(list(range(10)))
print("\n")

##### En el fichero de listas se mostrarán más funciones #####

#05 - TUPLAS - (No mutables)
newtupla = tuple()
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("######## 05-TUPLAS ########")
print(type(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#Consultando el elemento "Daniel" cuantas veces se encuentra en la tupla
print("El elemento se repite:",grupo1.count("Daniel"))

#Muestra el indice del primer elemento buscado
print("Indice del elemento:",grupo1.index ("Daniel"))

#Reasignando el primer elemento de la tupla
"""grupo1[0] = "Constanza"
print(grupo1)"""

#¿Se pueden sumar las tuplas?


#Obteniendo un trozo de la tupla
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("Trozo de la tupla",grupo2[0:3])

#¿Entonces como no puedo modificar una tupla, que puedo hacer?
#grupo1 = list(grupo1)
#print("La tupla ahora es de tipo:",type(grupo1),"\n")
print("\n")

#06 - SETS (Conjuntos) -  Estructura fija
#Formas de inicializar un Set
print("######## 06-SETS ########")
conjunto_vacio = set()
conjunto_vacio1 = {} #¿diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul","Rojo","Verde"}) #utilizando la funcion set
conjunto_animales = {"Gato","Perro","Loro"}     #utilizando corchetes

print(type(conjunto_colores)) #tipo de dato set
print(type(conjunto_animales)) #tipo de dato set
print("El primer set contiene los siguientes colores:",conjunto_colores)
print("El segundo set contiene los siguientes animales:",conjunto_animales)

#print(conjunto_animales[0]) #accediendo al primer elemento del set
conjunto_colores.add("Celeste")
print("El set de colores lo conforman:",conjunto_colores)                                            #un set es una estructura desordenada a diferencia de una Lista

#conjunto_animales.add("Gato")
print("El set de animales lo conforman:",conjunto_animales,"\n")                                     #un set no acepta duplicados, a diferencia de las listas que si.


#07 - DICCIONARIOS (Clave-Valor)
print("######## 06-DICCIONARIOS ########")

diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad":29
    }

print(datos_personales)

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad": 29,
    "Asignaturas": {"Estructura de Datos", "Programación"}
    }

print("Diccionario inicial:",datos_personales)

#Consulta la cantidad de elementos del Diccionario
print(len(datos_personales))

#Es facilmente accesible a los elementos dentro de un diccionario
print(datos_personales["Institucion"])

#¿Como actualizamos el valor de una clave dentro de un diccionario?
datos_personales["Institucion"] = "USS" 
print("Diccionario actualizado:",datos_personales)

#Agregando un nuevo campo al diccionario
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)
print("Diccionario con el nuevo campo:",datos_personales)

#Eliminando un campo del diccionario
del datos_personales["Ciudad"]
print("Diccionario con el campo eliminado:",datos_personales)

#08-¿Forzando el tipo de dato?
universidad: str = "Universidad de Los Lagos"
#universidad = 90
#universidad = True

#¿Al final que tipo de dato es la variable universidad?

