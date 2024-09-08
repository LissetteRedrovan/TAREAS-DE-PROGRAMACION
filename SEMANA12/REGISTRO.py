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
# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    for j, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)
        print(f'Ciudad {i+1}, Semana {j+1}: Promedio de temperatura = {promedio:.2f}°C')

