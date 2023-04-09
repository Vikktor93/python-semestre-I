###GUIA RÁPIDA TIPOS DE DATOS EN PYTHON

#01-DATOS DE TIPO NÚMERICO
estatura = 1.71
peso = 70.5
complejo =  1 + 4j

print("01-DATOS NÚMERICOS");
print("Mi estatura es de",estatura,"m","y mi peso de",peso,"kg")
print("Impresion de un número complejo:",complejo,"\n")


#Transformando un real a entero
print("Transformando un valor real a entero:",int(peso))

#OPERACION ARITMETICA BÁSICA
imc = peso/estatura**2
print("Mi IMC es de:",imc,"\n")

#02- DATOS DE TIPO CADENA DE CARACTERES 
asignatura = "Programación"
carrera = "Ingenieria Civil en Informática"
print("02-STRINGS")
print("La asignatura de",asignatura,"corresponde a la carrera de",carrera)

#Utilizando la función len (cuenta la cantidad de caracteres)
print("La cantidad de caracteres de la palabra", asignatura, "es de:",len(asignatura))
print("La cantidad de caracteres de la palabra", carrera, "es de:",len(carrera),"\n")


#03- VALORES BOOLEANOS
ampolleta = False
interruptor = True

#Con type sabemos el tipo de datos que estamos tratando
print("03-BOOLEANS")
print(ampolleta,interruptor)
print("La variable ampolleta es de tipo:",type(interruptor),"\n")

#04- DATOS TIPO ARRAY (Objetos de Tipo Colección)
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastián"]
num = [1,2,3,4,5,6]
print("04-ARREGLOS")
print(estudiantes)
print(num)

#05-PALABRAS RESERVADAS


