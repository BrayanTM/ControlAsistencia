"""
Sistema de reconocimiento facial para registrar ingresos de empleados.
Utiliza la librería face_recognition para detectar y reconocer caras en imágenes capturadas por
la cámara web. Los nombres de los empleados y sus imágenes deben estar almacenados en la carpeta
'employees'. Los registros de ingresos se guardan en un archivo CSV.
"""

import cv2
import face_recognition as fr
import os
import numpy as np
from _datetime import datetime

# Crear base de datos
ruta = 'employees'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)


for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


# Codificar las imagenes
def codificar_imagenes(imagenes):
    # Lista para almacenar las codificaciones
    lista_codificada = []

    # Pasar cada imagen a RGB y codificar
    for img in imagenes:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(img_rgb)[0]
        lista_codificada.append(codificado)
    return lista_codificada

# Registrar ingresos
def registrar_ingresos(persona):
    file = open('assists/assists.csv', 'r+')
    lista_registros = file.readlines()
    nombres_registrados = []
    for linea in lista_registros:
        ingreso = linea.split(',')
        nombres_registrados.append(ingreso[0])

    if persona not in nombres_registrados:
        ahora = datetime.now()
        string_hora = ahora.strftime('%H:%M:%S')
        file.writelines(f'\n{persona},{string_hora}')
    file.close()


lista_codificada_empleados = codificar_imagenes(mis_imagenes)


# Tomar una imagen de la camara y buscar coincidencias
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)


# Leer la imagen de la camara
while True:

    exito, imagen = captura.read()

    cv2.imshow("Capturando imagen", imagen)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


if not exito:
    print("No se ha podido tomar la imagen")
else:
    # Reconocer cara en la imagen
    cara_capturada = fr.face_locations(imagen)

    # Codificar la cara capturada
    cara_capturada_codificada = fr.face_encodings(imagen, cara_capturada)

    # Buscar coincidencias
    for cara_codificada, caraubic in zip(cara_capturada_codificada, cara_capturada):
        coincidencias = fr.compare_faces(lista_codificada_empleados, cara_codificada)
        distancias = fr.face_distance(lista_codificada_empleados, cara_codificada)

        indice_coincidencia = np.argmin(distancias)

        # Mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print('No coincide con ningun empleado')
        else:
            # Buscar el nombre del empleado al que pertenece la cara
            nombre_empleado = nombres_empleados[indice_coincidencia]

            # Crear un rectangulo alrededor de la cara
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre_empleado, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

            # Registrar el ingreso del empleado
            registrar_ingresos(nombre_empleado)

            # Mostrar la imagen con el nombre
            cv2.imshow('Igagen Web', imagen)
            # Mantener ventana abierta
            cv2.waitKey(0)