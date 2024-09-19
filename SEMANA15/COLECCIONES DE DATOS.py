#Datos de diccionario
informacion_personal = {
    "nombre": "lissette redrovan",
    "edad": 25,
    "ciudad": "Guayaquil",
    "profesion": "Policia"
}

#Acceder y modificar valores ciudad y profesion
informacion_personal["ciudad"] = "Riobamba"
informacion_personal["profesion"] = "Seguridad Ciudadana"

#Verificar si la clave "telefono" existe en el diccionario. Si no existe, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0980084253"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

print(informacion_personal)
