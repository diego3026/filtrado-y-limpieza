import csv

# Definir la función para reemplazar caracteres incorrectos
def corregir_caracteres(texto):
    return texto.replace('�', 'ñ')


def corregir(path):
    # Abrir el archivo CSV original para lectura
    with open(path, mode='r', encoding='utf-8') as archivo_original:
        lector_csv = csv.reader(archivo_original)
        
        # Leer las filas originales y corregir los caracteres
        filas_corregidas = []
        for fila in lector_csv:
            fila_corregida = [corregir_caracteres(celda) for celda in fila]
            filas_corregidas.append(fila_corregida)


    # Abrir un nuevo archivo CSV para escritura
    with open(path, mode='w', encoding='utf-8', newline='') as archivo_corregido:
        escritor_csv = csv.writer(archivo_corregido)
        
        # Escribir las filas corregidas en el nuevo archivo CSV
        for fila_corregida in filas_corregidas:
            escritor_csv.writerow(fila_corregida)

