""" Imprimir un string que muestre un mensaje en la terminal. 
Este mensaje deberá tener el siguiente formato: """

#    > Hola mi nombre es {nombre}, tengo {edad} años y en 20 años tendré {total_edad} años

""" Tener en cuenta que los datos se deben ingresar por consola
Además se debe calcular la edad que vas a tener en 20 años a partir de 
tu edad actual. Por ejemplo, si tienes actualmente 19 años, el mensaje 
deberá decir: "tengo 19 años y en 20 años tendré 39 años"""

### SOLUCIÓN

nombre = input("¿Cual es tu nombre?\n")
edad = input("¿Cual es tu edad?\n")
print(type(edad))
total_edad = int(edad) + 20

formato = f"Hola mi nombre es {nombre}, tengo {str(edad)} años y en 20 años tendré {str(total_edad)} años"
print(formato)