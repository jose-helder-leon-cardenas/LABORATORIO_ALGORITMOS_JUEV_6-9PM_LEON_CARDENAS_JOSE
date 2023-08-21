# “Soy profesor y me encanta inspirar y enseñar a la gente”.
#¿Cuántas palabras únicas se han utilizado en la frase? 
#Usa los métodos de split y sets para obtener las palabras únicas.

sentencia = "Soy profesor y me encanta inspirar y enseñar a la gente"
palabras = sentencia.split()
palabras_unicas = set(palabras)

num_palab_unicas= len(palabras_unicas)
print("Number of unique words:", num_palab_unicas)

