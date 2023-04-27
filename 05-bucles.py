#GUIA RÁPIDA BUCLESS/CICLOS EN PYTHON
# Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos


#01-WHILE
edad = 15
num = 0

#while edad > 18:
   # print("Eres menor de edad, no puedes manejar")

#¿Qué hace este bucle?
print("############ 01 - CICLO WHILE ############")
while num <= 100:
    print(num)
    num += 2
print("Primer Bucle terminado!\n")

#Combinando While y else
while num <= 200:
    print(num)
    num += 2
else: 
    print("Mi condicion es igual o mayor a 200")
print("Segundo Bucle terminado!")


#Combinando While y if
while num <= 300:
    print(num)
    num += 2
    if num == 250:  #mover if izquierda
        print("Mi condicion es igual a 250")
print("Tercer Bucle terminado!\n")

#Utilizando el break
while num <= 400:
    print(num)
    num += 2
    if num == 350:  #mover if izquierda
        print("Se detiene la ejecución")
        break
print(num)
print("Cuarto Bucle terminado!\n")


#Bucle For
print("############ 02 - CICLO FOR ############")

newlista = [0,1,2,3,4,5,6,7,8,9,10]

for i in newlista:
    print(i)