#GUIA RÁPIDA CONDICIONALES EN PYTHON
# Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

#CONDICIONAL IF
print('######## 01- UTILIZANDO IF y ELSE ########\n')

licencia = False
edad = 19
automovil = False

print('######## Utilizando el primer condicional IF ########')
if licencia:
    print('Puedo conducir porque tengo licencia\n')
else:
    print('No tengo licencia para conducir\n')
"""print("Este print fuera del else")"""


#¿Estará correcto este código?    
"""if licencia == True:
    print('Puedo conducir porque tengo licencia')
else:
    print('No tengo licencia para conducir')"""


print('######## Utilizando el segundo condicional IF ########')
if edad:
    print('Puedo conducir porque soy mayor de edad\n')
else:
    print('No puedo conducir soy menor de edad\n')
    

print('######## Utilizando el tercer condicional IF ########')
if edad >= 18:
    print('Puedo conducir porque soy mayor de edad\n')
else:
    print('No puedo conducir soy menor de edad\n')


print('######## 02 UTILIZANDO IF y ELIF, ELSE ########\n')
if licencia and edad >= 18:
    print('Puedo conducir porque soy mayor de edad y tengo licencia')
elif automovil:
    print('Tengo automovil, pero no tengo licencia ni la edad necesaria')
else:
    print('No puedo conducir no tengo ni la edad, ni licencia ni automovil')
    