documento = "archivo.txt"  # Nombre del archivo a leer
llave_aleatoria = "llave_aleatoria"  # Clave aleatoria para el XOR

# Leer los bytes del archivo
with open(documento, "rb") as archivo:
    bytes_documento = archivo.read()

# Repetir la clave iterativamente si los bytes son más que la longitud de la clave
llave_repetida = (llave_aleatoria * ((len(bytes_documento) // len(llave_aleatoria)) + 1))[:len(bytes_documento)]

# Realizar la operación XOR
bytes_resultantes = bytes([a ^ b for a, b in zip(bytes_documento, llave_repetida.encode())])

with open("archivo_cifrado.bin", "wb") as archivo:
    archivo.write(bytes_resultantes)
