"""
EJERCICIO:
Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
  recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
  interpolación, verificación...
DIFICULTAD EXTRA (opcional):
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
- Palíndromos
- Anagramas
- Isogramas
"""

""" 
Operaciones
"""



s1 = 'Hola'
s2 = 'Python'

# Concatenación
print(s1 + ', ' + s2 + '!')

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] +s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Búsqueda
print('a' in s1)
print('i' in s1)

# Reemplazo
print(s1.replace('o', 'a'))

# División 
print(s2.split('t'))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print('joseph code'.title())
print('joseph code'.capitalize())

# Eliminación de espacios al principio y al final
print(' joseph code '.strip())

# Búsqueda al principio y al final
print(s1.startswith('Ho'))
print(s1.startswith('Py'))
print(s1.endswith('la'))
print(s1.endswith('thon'))

s3 = 'Code Joseph @joseph'

# Búsqueda de posición
print(s3.find('joseph'))
print(s3.find('Joseph'))
print(s3.find('J'))
print(s3.lower().find('j'))

# Búsqueda de ocurrecias
print(s3.lower().count('j'))

# Formateo
print('Saludo: {}, lenguaje: {}!'.format(s1,s2))

# Interpolación
print(f'Saludo: {s1}, lenguaje: {s2}!')

# Transformación en lista de carácteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ', ', s2, '!']
print(''.join(l1))

# Transformaciones numéricas
s4 = '123456'
s4 = int(s4)
print(s4)

s5 = '123456.123'
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 ='123456'
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

""" 
Extra
"""
# Programa para analizar dos palabras y verificar si son palíndromos, anagramas e isogramas

def es_palindromo(palabra):
    """Verifica si una palabra es un palíndromo."""
    palabra_limpia = ''.join(filter(str.isalnum, palabra.lower()))
    return palabra_limpia == palabra_limpia[::-1]

def es_anagrama(palabra1, palabra2):
    """Verifica si dos palabras son anagramas."""
    palabra1_limpia = sorted(filter(str.isalnum, palabra1.lower()))
    palabra2_limpia = sorted(filter(str.isalnum, palabra2.lower()))
    return palabra1_limpia == palabra2_limpia

def es_isograma(palabra):
    """Verifica si una palabra es un isograma."""
    palabra_limpia = ''.join(filter(str.isalpha, palabra.lower()))
    return len(palabra_limpia) == len(set(palabra_limpia))

def analizar_palabra(palabra):
    """Analiza si una palabra es palíndromo e isograma."""
    resultados = {
        'palindromo': es_palindromo(palabra),
        'isograma': es_isograma(palabra)
    }
    return resultados

def main():
    # Solicitar las palabras al usuario
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")

    # Analizar las palabras individualmente
    resultados_palabra1 = analizar_palabra(palabra1)
    resultados_palabra2 = analizar_palabra(palabra2)

    # Mostrar resultados para la primera palabra
    print(f"\nAnálisis de la palabra '{palabra1}':")
    print("- Es un palíndromo." if resultados_palabra1['palindromo'] else "- No es un palíndromo.")
    print("- Es un isograma." if resultados_palabra1['isograma'] else "- No es un isograma.")

    # Mostrar resultados para la segunda palabra
    print(f"\nAnálisis de la palabra '{palabra2}':")
    print("- Es un palíndromo." if resultados_palabra2['palindromo'] else "- No es un palíndromo.")
    print("- Es un isograma." if resultados_palabra2['isograma'] else "- No es un isograma.")

    # Analizar si son anagramas entre sí
    if es_anagrama(palabra1, palabra2):
        print(f"\nLas palabras '{palabra1}' y '{palabra2}' son anagramas.")
    else:
        print(f"\nLas palabras '{palabra1}' y '{palabra2}' no son anagramas.")

if __name__ == "__main__":
    main()