# Simulación de un "buffer" que solo puede almacenar un número limitado de datos
buffer = []  # Aquí guardaremos los datos
tamaño_maximo = 3  # Definimos el tamaño del buffer

# Lista de datos que queremos guardar
datos = ["Hola", "Mundo", "Python", "Overflow"]

# Agregamos los datos al buffer
for dato in datos:
    if len(buffer) < tamaño_maximo:
        buffer.append(dato)
        print(f"Guardando: {dato}")
    else:
# El buffer está lleno: eliminar el más antiguo y agregar el nuevo
       eliminado = buffer.pop(0)
       buffer.append(dato)
       print(f"¡El buffer esta lleno!. Se eliminó '{eliminado}' y se guardó: {dato}")

# Mostramos el contenido final del buffer
print("\nContenido del buffer:", buffer)