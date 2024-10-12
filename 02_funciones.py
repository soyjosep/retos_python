"""
EJERCICIO:
- Crea ejemplos de funciones básicas que representen las diferentes
  posibilidades del lenguaje:
  Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable LOCAL y GLOBAL.
- Debes hacer print por consola del resultado de todos los ejemplos.
  (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
DIFICULTAD EXTRA (opcional):
Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
  - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
  - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
  - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
  - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
"""

"""
Funciones definidas por el usuario mejoradas
"""

# Sin parámetros ni retorno
def greet():
    """Imprime un saludo simple."""
    print("Hola Python")

greet()

# Con retorno
def return_greet():
    """Retorna un saludo."""
    return "Hola Python"

print(return_greet())

# Con un argumento
def arg_greet(name: str):
    """Imprime un saludo personalizado con el nombre proporcionado."""
    print(f"Hola, {name}")

arg_greet("Joseph")

# Con varios argumentos
def args_greet(greet: str, name: str):
    """Imprime un saludo personalizado utilizando varios argumentos."""
    print(f"{greet}, {name}")

args_greet("Hi", "Joseph")
args_greet(name="Joseph", greet="Hi")

# Con un argumento predeterminado
def default_arg_greet(name: str = "Python"):
    """Imprime un saludo con un nombre predeterminado o personalizado."""
    print(f"Hola, {name}")

default_arg_greet("Joseph")
default_arg_greet()

# Con varios argumentos y retorno
def return_args_greet(greet: str, name: str) -> str:
    """Retorna un saludo personalizado usando varios argumentos."""
    return f"{greet}, {name}"

print(return_args_greet("Hi", "Joseph"))

# Con retorno de varios valores
def multiple_return_greet() -> tuple:
    """Retorna múltiples valores como una tupla."""
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos
def variable_arg_greet(*names: str):
    """Imprime saludos para múltiples nombres usando un número variable de argumentos."""
    for name in names:
        print(f"Hola, {name}")

variable_arg_greet("Python", "Joseph", "Trix", "Comunidad")

# Con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names: str):
    """Imprime saludos usando un número variable de argumentos clave-valor."""
    for key, value in names.items():
        print(f"Hola, {value} ({key})")

variable_key_arg_greet(
    language="Python",
    name="Joseph",
    alias="Joseph Code",
    age="34"  # Mejor usar str para mantener consistencia en los saludos
)

"""
Funciones dentro de funciones mejoradas
"""

def outer_function():
    """Función que contiene una función interna."""
    def inner_function():
        """Función interna que imprime un mensaje."""
        print("Función interna: ¡Hola Python!")
    
    # Llamamos a la función interna
    inner_function()

outer_function()

"""
Funciones del lenguaje (built-in) mejoradas
"""

# Utilización de funciones integradas en Python
print(len("JosephCode"))  # Longitud de la cadena
print(type(36))  # Tipo de dato
print("josephcode".upper())  # Convertir a mayúsculas

"""
Variables locales y globales mejoradas
"""

global_var = "Python"  # Variable global

def hello_python():
    """Imprime una combinación de variables locales y globales."""
    local_var = "Hola"  # Variable local
    print(f"{local_var}, {global_var}")

# Uso correcto de variables locales y globales
print(global_var)  # Imprime la variable global
hello_python()

# Ejemplo de modificación de una variable global dentro de una función
def modify_global_var():
    global global_var  # Declaramos que queremos modificar la variable global
    global_var = "Python mejorado"
    print(f"Variable global modificada: {global_var}")

modify_global_var()

"""
Dificultad extra mejorada
"""

def print_numbers(text_1: str, text_2: str) -> int:
    """
    Imprime números del 1 al 100, sustituyendo múltiplos de 3 y 5 por textos proporcionados.
    Retorna la cantidad de números que fueron impresos en lugar de los textos.
    
    Parámetros:
    - text_1 (str): Texto a imprimir para múltiplos de 3.
    - text_2 (str): Texto a imprimir para múltiplos de 5.

    Retorno:
    - int: El número de veces que se imprimieron números en lugar de los textos.
    """
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

# Llamamos a la función y almacenamos el resultado
result = print_numbers("Fizz", "Buzz")
print(f"Se imprimieron números en lugar de texto {result} veces.")