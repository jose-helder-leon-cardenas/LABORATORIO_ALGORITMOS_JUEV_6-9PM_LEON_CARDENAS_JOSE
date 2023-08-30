from countries_data import countries

"""paises_mas_poblados = sorted(countries, key=lambda x: x["population"], reverse=True)[:10]

print("paises mas poblados son: \n ")

for pais in paises_mas_poblados:
    print(pais["name"])
"""

sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)
top_populated_countries = sorted_countries[:10]

print("Top 10 most populated countries:")
for country in top_populated_countries:
    print(f"{country['name']}: {country['population']} people")
    