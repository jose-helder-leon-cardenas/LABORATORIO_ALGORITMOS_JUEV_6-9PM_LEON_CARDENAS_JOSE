frase = "ána"

# Eliminar tildes, convertir a minúsculas y eliminar espacios
frase = frase.lower()
frase_sin_tildes = ''
for letra in frase:
    if letra in ('á', 'é', 'í', 'ó', 'ú'):
        letra = 'a' if letra == 'á' else 'e' if letra == 'é' else 'i' if letra == 'í' else 'o' if letra == 'ó' else 'u'
    if letra.isalpha():
        frase_sin_tildes += letra

# Verificar si es un palíndromo
es_palindromo = frase_sin_tildes == frase_sin_tildes[::-1]

# Imprimir resultado
if es_palindromo:
    print(f'"{frase}" es un palíndromo.')
else:
    print(f'"{frase}" no es un palíndromo.')



























































































































































































































"""def es_palindromo(frase):
    # Eliminar tildes y convertir a minúsculas
    frase = frase.lower()
    frase = ''.join(c for c in frase if not c in ('á', 'é', 'í', 'ó', 'ú'))
    
    # Eliminar espacios
    frase = frase.replace(" ", "")
    
    # Verificar si es un palíndromo
    return frase == frase[::-1]

# Ejemplo de uso
frase = "ána"
if es_palindromo(frase):
    print(f'"{frase}" es un palíndromo.')
else:
    print(f'"{frase}" no es un palíndromo.')"""

"""def eliminar_tildes(frase):
    tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
    return ''.join(tildes.get(c, c) for c in frase)

def es_palindromo(frase):
    # Eliminar tildes, convertir a minúsculas y eliminar espacios
    frase = eliminar_tildes(frase.lower().replace(" ", ""))
    return frase == frase[::-1]

# Ejemplo de uso
frase = "ána"
if es_palindromo(frase):
    print(f'"{frase}" es un palíndromo.')
else:
    print(f'"{frase}" no es un palíndromo.')"""