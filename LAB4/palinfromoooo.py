frase = input("ingrese una palabra, veamos si es palindromo : ")  # ána

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
