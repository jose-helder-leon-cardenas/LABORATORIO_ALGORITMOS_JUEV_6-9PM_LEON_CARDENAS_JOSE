persona = {
    'first_name': 'Edem',
    'last_name': 'Terraza',
    'age': 31,
    'country': 'Peru',
    'is_married': True, #
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

# A) Comprueba si el diccionario de la persona tiene la clave de habilidades; 
# si es así, imprime la habilidad del medio en la lista de habilidades

if 'skills' in persona:
    habilidades = persona['skills']
    indice_habilidad_media = len(habilidades) // 2
    habilidad_media = habilidades[indice_habilidad_media]
    print("\nHabilidad media:b ", habilidad_media, "\n")
else:
    print("\nNo se encontraron habilidades en el diccionario de la persona.\n")

# B) Comprueba si el diccionario de la persona tiene la clave de habilidades; 
# si es así, verifica si la persona tiene la habilidad 'Python' e imprime el resultado

if 'skills' in persona:
    habilidades = persona['skills']
    if 'Python' in habilidades:
        print("\nLa persona tiene la habilidad Python.\n")
    else:
        print("\nLa persona no tiene la habilidad Python.\n")
else:
    print("\nNo se encontraron habilidades en el diccionario de la persona.\n")

# C) Si las habilidades de una persona tienen solo JavaScript y React, imprime ('Él es un desarrollador frontend'), 
# si las habilidades de la persona tienen Node, Python, MongoDB, imprime ('Él es un desarrollador backend'), 
# si las habilidades de la persona tienen React, Node y MongoDB, imprime ('Él es un desarrollador fullstack'), 
# de lo contrario imprime ('título desconocido') - ¡para obtener resultados más precisos, se pueden anidar más condiciones!

skills = persona.get('skills', [])

if 'JavaScript' in skills and 'React' in skills:
    print('\nÉl es un desarrollador frontend\n')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('\nÉl es un desarrollador backend\n')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('\nÉl es un desarrollador fullstack\n')
else:
    print('\ntítulo desconocido\n')

