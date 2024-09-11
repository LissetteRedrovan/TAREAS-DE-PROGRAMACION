#Registo ciudad(3)xsemana(4)xdias(7)
temperaturas = [
    #Guayaquil
    [
        [35, 35, 32, 30, 28, 39, 30],  #semanas 1
        [25, 33, 28, 20, 35, 28, 26],  #semana 2
        [30, 27, 28, 31, 28, 23, 19],  #semana 3
        [28, 20, 26, 22, 30, 33, 36]  #semana 4
    ],
    #Quito
    [
        [23, 25, 32, 30, 28, 39, 30],  #Semana 1
        [25, 32, 34, 36, 37, 28, 26],  #Semana 2
        [32, 34, 28, 26, 25, 23, 18],  #Semana 3
        [28, 25, 26, 22, 32, 32, 36]  #Semana 4
    ],
    #Riobamba
    [
        [8, 10, 5, 11, 12, 13, 14],  #Semana 1
        [12, 6, 7, 12, 17, 12, 5],  #Semana 2
        [6, 12, 13, 8, 12, 9, 10],  #Semana 3
        [5, 4, 11, 12, 15, 5, 17]  #Semana 4
    ],
]
#calcule la temperatura promedio de una ciudad durante un período de tiempo.
def calcular_temperatura_promedio(datos_temperaturas):
    promedios = []
    for ciudad in datos_temperaturas:
        suma_total = 0
        contador_dias = 0
        for semana in ciudad:
            suma_semana = sum(semana)
            dias_semana = len(semana)
            suma_total += suma_semana
            contador_dias += dias_semana
        promedio_ciudad = suma_total / contador_dias
        promedios.append(promedio_ciudad)
    return promedios
promedios_ciudades = calcular_temperatura_promedio(temperaturas)
print(promedios_ciudades)