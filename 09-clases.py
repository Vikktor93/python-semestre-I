# GUIA RÁPIDA DE CLASES Y OBJETOS EN PYTHON
# Docente: Victor Saldivia Vera
# Universidad de Los Lagos
class Persona(): 
        # Atributos de Clase (Características compartidas por todos los objetos de la clase)
        nombre = "Cristina" 
        apellido = "Torres"
        edad = 23
        
        # Métodos (Comportamientos)
        def estudiar(self):
            print(f"{self.nombre} esta estudiando")
        
        def dormir(self):
            print(f"{self.nombre} esta durmiendo")
            
# Creación de un objeto de la clase Persona
persona1 = Persona()

# Acceso a los atributos y métodos del objeto
print(f"Nombre: {persona1.nombre}")
print(f"Apellido: {persona1.apellido}")
print(f"Edad: {persona1.edad} años")

# Llamando a los métodos de la Clase
persona1.estudiar()
persona1.dormir()