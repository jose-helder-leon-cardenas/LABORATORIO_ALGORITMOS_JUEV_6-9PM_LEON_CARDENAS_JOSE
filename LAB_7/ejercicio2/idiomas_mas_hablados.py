from countries_data import countries

idiomas_totales = []

for pais in countries:
    idiomas_pais = pais["languages"]
    idiomas_totales.extend(idiomas_pais)

numero_idiomas = len(set(idiomas_totales))

print("\nlos primeros 10 idiomas mas hableados son : ",numero_idiomas , "\n")
