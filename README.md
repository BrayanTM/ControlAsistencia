# Sistema de reconocimiento facial para registrar ingresos de empleados

Este proyecto implementa un sistema de reconocimiento facial automatizado para registrar los ingresos de empleados utilizando visión por computadora y aprendizaje automático.

## Descripción

El sistema utiliza la librería `face_recognition` para detectar y reconocer caras en tiempo real a través de la cámara web. Compara las caras capturadas con una base de datos de empleados previamente registrados y automáticamente registra los ingresos en un archivo CSV con la hora correspondiente.

## Características principales

- **Reconocimiento facial en tiempo real**: Utiliza la cámara web para capturar y analizar caras
- **Base de datos de empleados**: Almacena las imágenes de referencia de los empleados
- **Registro automático de ingresos**: Guarda automáticamente la hora de ingreso en formato CSV
- **Prevención de registros duplicados**: Evita registrar múltiples ingresos del mismo empleado
- **Interfaz visual**: Muestra el nombre del empleado reconocido en pantalla
- **Detección de empleados no registrados**: Identifica cuando una cara no coincide con ningún empleado

## Requisitos del sistema

### Dependencias

Las siguientes librerías son necesarias para el funcionamiento del sistema:

```
opencv-python
face-recognition
numpy
```

### Hardware requerido

- Cámara web funcional
- Sistema operativo compatible con OpenCV
- Python 3.6 o superior

## Estructura del proyecto

```
ControlAsistencia/
│
├── main.py                    # Archivo principal del sistema
├── README.md                  # Documentación del proyecto
├── requeriments.txt           # Dependencias del proyecto
├── employees/                 # Carpeta con imágenes de empleados
│   ├── Brayan Tebelan.jpg
│   ├── Cosmo Kramer.jpg
│   ├── Elaine Benes.jpg
│   ├── Federico Garay.jpg
│   ├── George Constanza.jpg
│   └── Jerry Seinfeld.jpg
└── assists/                   # Carpeta para registros de asistencia
    └── assists.csv            # Archivo CSV con los registros
```

## Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar las dependencias**:
   ```bash
   pip install -r requeriments.txt
   ```

3. **Configurar la base de datos de empleados**:
   - Colocar las imágenes de los empleados en la carpeta `employees/`
   - Los nombres de los archivos deben corresponder al nombre del empleado
   - Formato recomendado: `Nombre Apellido.jpg`

4. **Crear la carpeta de asistencias**:
   - Asegurarse de que existe la carpeta `assists/`
   - El archivo `assists.csv` se creará automáticamente

## Uso

1. **Ejecutar el programa**:
   ```bash
   python main.py
   ```

2. **Interacción con el sistema**:
   - El sistema abrirá la cámara web automáticamente
   - Presionar `q` para salir del modo de captura y procesar la imagen
   - El sistema reconocerá automáticamente las caras y registrará los ingresos

3. **Visualización de resultados**:
   - Si se reconoce un empleado, se mostrará su nombre en pantalla
   - El ingreso se registrará en `assists/assists.csv`
   - Si no se reconoce la cara, se mostrará un mensaje indicándolo

## Funcionamiento técnico

### Componentes principales

1. **Carga de la base de datos**:
   - Lee todas las imágenes de la carpeta `employees/`
   - Extrae los nombres de los archivos como identificadores de empleados

2. **Codificación de imágenes**:
   - Convierte las imágenes a formato RGB
   - Genera codificaciones faciales únicas para cada empleado
   - Utiliza algoritmos de deep learning para la extracción de características

3. **Captura en tiempo real**:
   - Utiliza OpenCV para acceder a la cámara web
   - Captura frames continuamente hasta que el usuario presiona 'q'

4. **Reconocimiento facial**:
   - Detecta caras en la imagen capturada
   - Compara las codificaciones con la base de datos
   - Utiliza distancia euclidiana para determinar coincidencias

5. **Registro de asistencias**:
   - Verifica si el empleado ya fue registrado en el día
   - Guarda el nombre y la hora de ingreso en formato CSV
   - Previene registros duplicados

### Parámetros de configuración

- **Umbral de reconocimiento**: 0.6 (distancia máxima para considerar una coincidencia)
- **Formato de hora**: HH:MM:SS
- **Formato de salida**: CSV con columnas "Nombre,Hora"

## Archivo de salida

El sistema genera un archivo `assists/assists.csv` con el siguiente formato:

```csv
Nombre Empleado,Hora
Federico Garay,09:15:30
Brayan Tebelan,09:22:45
Jerry Seinfeld,09:35:12
```

## Limitaciones

- El sistema requiere buena iluminación para un reconocimiento óptimo
- Solo reconoce una cara por sesión de captura
- Las imágenes de referencia deben ser de buena calidad y mostrar claramente el rostro
- No incluye funcionalidades de registro de salida

## Solución de problemas

### Problemas comunes

1. **Error "No se ha podido tomar la imagen"**:
   - Verificar que la cámara web esté conectada y funcionando
   - Comprobar que no esté siendo utilizada por otra aplicación

2. **No se reconoce ningún empleado**:
   - Ajustar la iluminación del ambiente
   - Verificar la calidad de las imágenes de referencia
   - Considerar ajustar el umbral de reconocimiento

3. **Errores de importación**:
   - Instalar todas las dependencias listadas en `requeriments.txt`
   - Verificar la compatibilidad de versiones de Python

## Contribución

Para contribuir al proyecto:

1. Realizar un fork del repositorio
2. Crear una rama para la nueva funcionalidad
3. Implementar los cambios
4. Realizar pruebas exhaustivas
5. Enviar un pull request

## Licencia

Este proyecto es de código abierto y está disponible bajo los términos de la licencia especificada en el repositorio.

---

**Nota**: Este sistema está diseñado para uso interno y educativo. Para implementaciones en producción, se recomienda adicionar medidas de seguridad adicionales y cumplir con las regulaciones locales de privacidad de datos.
