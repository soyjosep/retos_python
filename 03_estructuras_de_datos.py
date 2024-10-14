"""
EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto
  en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización
  y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar,
  y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más
  de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.
"""

# Listas

my_list = ["Joseph", "Black", "Wolfy", "Visionos"]
print(my_list)
my_list.append("Castor") # Inserción
print(my_list)
my_list.remove("Visionos") # Eliminación
print(my_list)
print(my_list[3]) # Acceso
my_list[3] = "Temple" # Actualización
print(my_list)
my_list.sort() # Ordenación
print(my_list)
print(type(my_list))

# Tuplas

my_tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1]) # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets

