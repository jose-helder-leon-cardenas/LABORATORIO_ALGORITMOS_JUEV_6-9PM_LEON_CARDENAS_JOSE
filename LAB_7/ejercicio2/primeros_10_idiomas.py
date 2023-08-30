from countries_data import countries

frecuencia_idiomas = {}

for pais in countries:
    idiomas_pais = pais["languages"]
    for idioma in idiomas_pais:
        if idioma in frecuencia_idiomas:
            frecuencia_idiomas[idioma] += 1
        else:
            frecuencia_idiomas[idioma] = 1

idiomas_mas_hablados = sorted(frecuencia_idiomas, key=frecuencia_idiomas.get, reverse=True)[:10]

print("los idiomas mas hablados en la lista de diccionarios son : \n",idiomas_mas_hablados)
