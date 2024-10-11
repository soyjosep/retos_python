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
Funciones definidas por el usuario
"""

# Simple
def greet():
    print("hola python")
greet()

# Con retorno
def return_greet():
    return "Hola python"
print(return_greet)

# Con un argumento
def arg_greet(name):
    print(f"Hola, {name}")
arg_greet("Joseph")

# Con argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}")
args_greet("Hi", "Joseph")
args_greet(name="Joseph", greet="Hi, ")

# Con un argumento predeterminado
def default_arg_greet(name="Python"):
    print(f"Hola, {name}")
default_arg_greet("Joseph")
default_arg_greet()

# Con argumentos y return
def return_args_greet(greet, name):
    return f"{greet}, {name}"
print(return_args_greet("hi", "Joseph"))

# Con retorno de varios valores
def multiple_return_greet():
    return "Hola", "Python"
greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos
def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}")
variable_arg_greet("Python", "Joseph", "Trix", "Comunidad")

# Con un número variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola, {value} ({key})")
variable_key_arg_greet(
    lamguage="Python",
    name="Joseph",
    alias="Joseph Code",
    age= 34)

"""
Funciones dentro de funciones  
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola python!")
    inner_function()
outer_function()

"""
Funciones del lenguaje(built-in)
"""

print(len("JosephCode"))
print(type(36))
print("josephcode".upper())

"""
Variables locales y globales
"""

global_var = "Python"
def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}")
print(global_var)
# print(local_var) No se puede acceder desde fuera de la función
hello_python()

