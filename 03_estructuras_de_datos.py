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

my_list: list = ["Joseph", "Black", "Wolfy", "Visionos"]
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

my_tuple: tuple = ("Joseph", "Black", "Wolfy", "Visionos")
print(my_tuple[1]) # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets

my_set: set = {"Joseph", "Black", "Wolfy", "Visionos"}
print(my_set)
my_set.add("josephcode@gmail.com") # Inserción
my_set.add("josephcode@gmail.com") # No permite duplicados
print(my_set)
my_set.remove("Visionos") # Eliminación
print(my_set)
my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario

my_dict: dict = {
    "name": "Joseph",
    "surname": "Code",
    "alias": "@temple",
    "age": "34"
}
my_dict["email"] = "josephcode@gmail.com" # Insercion
print(my_dict)
del my_dict["surname"] # Eliminación
print(my_dict["name"]) # Acceso
my_dict["age"] = "37" # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenación
print(my_dict)
print(type(my_dict))

""" 
Extra
"""

def my_agenda():

    agenda = {}

    def insert_contact(name):
        phone = input("Introduce el teléfono del contacto: ")
        if phone.isdigit() and 6 <= len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Debes introducir un número de teléfono de 6 a 11 dígitos.")

    while True:
        print("\n1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ").strip()
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre del contacto: ").strip()
                if name:
                    insert_contact(name)
                else:
                    print("El nombre no puede estar vacío.")
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ").strip()
                if name in agenda:
                    insert_contact(name)
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ").strip()
                if name in agenda:
                    del agenda[name]
                    print(f"El contacto {name} ha sido eliminado.")
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

my_agenda()