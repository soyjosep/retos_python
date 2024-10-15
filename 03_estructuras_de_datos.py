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

    def is_valid_phone(phone):
        """Valida que el teléfono tenga entre 6 y 11 dígitos y sea numérico."""
        return phone.isdigit() and 6 <= len(phone) <= 11

    def get_valid_name():
        """Solicita al usuario un nombre válido (no vacío)."""
        while True:
            name = input("Introduce el nombre del contacto: ").strip()
            if name:
                return name
            else:
                print("El nombre no puede estar vacío.")

    def get_valid_phone():
        """Solicita al usuario un número de teléfono válido."""
        while True:
            phone = input("Introduce el teléfono del contacto (6-11 dígitos): ").strip()
            if is_valid_phone(phone):
                return phone
            else:
                print("Número de teléfono no válido. Debe tener entre 6 y 11 dígitos.")

    def search_contact(name):
        """Busca un contacto en la agenda."""
        if name in agenda:
            print(f"El número de teléfono de {name} es {agenda[name]}.")
        else:
            print(f"El contacto {name} no existe.")

    def insert_contact(name):
        """Inserta un nuevo contacto en la agenda."""
        if name in agenda:
            print(f"El contacto {name} ya existe.")
        else:
            phone = get_valid_phone()
            agenda[name] = phone
            print(f"Contacto {name} añadido con éxito.")

    def update_contact(name):
        """Actualiza el teléfono de un contacto existente."""
        if name in agenda:
            phone = get_valid_phone()
            agenda[name] = phone
            print(f"Contacto {name} actualizado con éxito.")
        else:
            print(f"El contacto {name} no existe.")

    def delete_contact(name):
        """Elimina un contacto de la agenda."""
        if name in agenda:
            del agenda[name]
            print(f"Contacto {name} eliminado con éxito.")
        else:
            print(f"El contacto {name} no existe.")

    def menu():
        """Muestra el menú y retorna la opción seleccionada."""
        print("\n1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        return input("Selecciona una opción: ")

    while True:
        option = menu()

        match option:
            case "1":
                name = get_valid_name()
                search_contact(name)
            case "2":
                name = get_valid_name()
                insert_contact(name)
            case "3":
                name = get_valid_name()
                update_contact(name)
            case "4":
                name = get_valid_name()
                delete_contact(name)
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 5.")

my_agenda()