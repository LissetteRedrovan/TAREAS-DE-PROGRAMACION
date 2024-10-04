#Escritura de Archivo de Texto
#Abre el archivo en modo de escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribe tres líneas de notas personales
    file.write("cuadernos.\n")
    file.write("lapiceros.\n")
    file.write("borradores.\n")

#Lectura de Archivo de Texto
#Abrir el archivo en modo de lectura ('r')
with open('my_notes.txt', 'r') as file:
# Lee el contenido del archivo línea por línea
    for line in file:
        print(line, end='')



