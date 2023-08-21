sentence = "the cat in the hat is in the house" 
palabra = sentence.split()
unica = list(set(palabra))
duplicado = set(palabras for palabras in palabra if palabra.count(palabras) > 1)
resultado = (unica, duplicado)
print(resultado)