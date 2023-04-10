#GUIA RÁPIDA DE OPERACIONES/OPERADORES EN PYTHON

#Partiremos con los operadores más comunes 
#01-OPERADORES ARITMETICOS

#Declarando variables de tipo entero
a = 20
b = 5
c = 4
d = 20

#Operaciones comunes
print("01-OPERADORES ARITMETICOS")
print("Suma entre a + b es:",a + b)
print("Resta entre a - b es:",a - b)
print("Multiplicación entre a * b es:",a * b)
print("División entre a / b es:",a / b)
print("El módulo entre a y b es:",a % b)
print("El cociente entre b / c es:",b // c)
print("El resultado de b elevado a c (5^4):",b**c)

#¿Se puede realizar esta operación? ¿Multiplicar un String por un entero?
print("Hola" * 5)

#¿y la siguiente multiplicación?
#print("Hola" * 3.5*2)



#Si el resultado es un 7 (numero entero), ¿por qué sale error?

#¿y esta operación un poco mas elaborada?
print("Hola" * (int((10*2)/5)),"\n")

#¿y por último esta operación de suma?
#print("Hola" + 20)

#02-OPERADORES DE COMPARACIÓN
print("02-OPERADORES DE COMPARACIÓN")

#Comparando términos númericos
print("Comparando Números")
print(a==b) #igual a
print(a!=b) #desigual a
print(a>b)  #mayor que
print(a<b)  #menor que
print(c>=d) #mayor o igual que
print(c<=d) #menor o igual que
print("\n")

#Comparando cadenas de caracteres
animal_domestico = "gato"
animal_salvaje= "leopardo"

print("Comparando Cadenas de Caracteres")
print(animal_domestico == animal_salvaje) #igual a
print(animal_domestico != animal_salvaje) #desigual a
print(animal_domestico > animal_salvaje)  #mayor que
print(animal_domestico < animal_salvaje)  #menor que
print(animal_domestico>=animal_salvaje)   #mayor o igual que
print(animal_domestico<=animal_salvaje)   #menor o igual que

#03-OPERADORES LÓGICOS

