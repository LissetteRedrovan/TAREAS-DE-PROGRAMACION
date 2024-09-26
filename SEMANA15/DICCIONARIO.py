#Datos del diccionario
informacion_personal = {
    "nombre": "Lissette Redrovan",
    "edad": 25,
    "ciudad": "Guayaquil",
    "profesion": "Policia"
}

#Acceder y modificar la ciudad
informacion_personal["ciudad"] = "Riobamba"
informacion_personal["profesion"] = "Seguridad ciudadana"

#Agregar una nueva clave-valor
informacion_personal["telefono"] = "0980084275"

#Eliminar la clave "edad"
del informacion_personal["edad"]

#Imprimir el diccionario resultante
print (informacion_personal)