'''RETO 2: Elaborar un algoritmo que sea capaz de solicitar la edad del
#usuario, pero que permita solo el ingreso de números, no de caracteres,
#además tiene que ser una edad válida.'''

while True:
    edad = input("Ingrese su edad: ")
    if edad.isdigit() and int(edad) >= 1:
        print(f"Su edad es de {edad} años")
        break
    else:
        print("Debe ingresar una edad válida por favor")
