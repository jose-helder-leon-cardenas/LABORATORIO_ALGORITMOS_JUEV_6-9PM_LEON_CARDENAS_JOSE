from countries_data16 import countries


def obtener_paises_mas_poblados(num_paises=10):
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    paises_mas_poblados = [pais['name'] for pais in sorted_countries[:num_paises]]

    return paises_mas_poblados

paises_mas_poblados = obtener_paises_mas_poblados(20)
for pais in paises_mas_poblados:
    print(pais)


############################
"""
def obtener_paises_mas_poblados(num_paises=10):
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    paises_mas_poblados = [pais['name'] for pais in sorted_countries[:num_paises]]

    return paises_mas_poblados

paises_mas_poblados = obtener_paises_mas_poblados(20)
print(paises_mas_poblados)
"""