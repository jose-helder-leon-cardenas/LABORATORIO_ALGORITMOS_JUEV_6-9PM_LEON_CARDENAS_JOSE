from countries_data16 import countries

# a) Crea una función llamada los idiomas más hablados en el mundo. 
#Debería devolver los 10 o 20 idiomas más hablados en el mundo en orden descendente

def paises_mas_poblados():
    # Ordenar la lista de países por población en orden descendente
    paises_ordenados = sorted(countries, key=lambda x: x['population'], reverse=True)
    
    # Tomar los primeros 10 o 20 países de la lista ordenada
    paises_seleccionados = paises_ordenados[:20]  # Puedes ajustar este número según tus necesidades
    
    # Devolver la lista de países seleccionados
    return paises_seleccionados


paises = paises_mas_poblados()
for pais in paises:
    print(pais['name'], pais['population'])


####################################

"""
def get_most_spoken_languages(num_languages=10):
    language_count = {}

    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    top_languages = [language[0] for language in sorted_languages[:num_languages]]

    return top_languages

most_spoken_languages = get_most_spoken_languages(20)
print(most_spoken_languages)
"""
##############################
"""
from collections import Counter

def obtener_idiomas_mas_hablados_mundo(paises, n):
    idiomas = []
    for pais in paises:
        idiomas.extend(pais["languages"])

    conteo_idiomas = Counter(idiomas)
    top_idiomas = conteo_idiomas.most_common(n)

    return top_idiomas

# Prueba la función
top_10_idiomas = obtener_idiomas_mas_hablados_mundo(countries, 10)
print(top_10_idiomas)

top_20_idiomas = obtener_idiomas_mas_hablados_mundo(countries, 20)
print(top_20_idiomas)

    """