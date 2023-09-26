# Youtube Downloader
Este es un sencillo script de Python que utiliza la biblioteca Pytube para descargar videos y audio de YouTube. El script te permite ingresar un enlace de YouTube y luego elegir si deseas descargar el video en alta calidad o solo el audio con formato MP3.

## Requisitos
- Python 3.x
- Pytube (`pip install pytube`)

## Uso
### v.1.0.0 (terminal)
1. Ejecuta el script `youdownloader.py` en tu entorno de Python.

2. El script te pedirá que ingreses el enlace del video de YouTube que deseas descargar.

3. Luego, el script te preguntará si deseas descargar el video o solo el audio:
   - Para descargar el audio, ingresa "1".
   - Para descargar el video, ingresa "2".
   - Para salir del programa, ingresa "3".

4. El script descargará el contenido seleccionado en la carpeta `./media` en tu directorio de trabajo actual.

## Ejemplo de Uso
Ingresa el siguiente comando en tu terminal: <br>
`python youdownoalder.py`

Claro, aquí tienes el archivo readme.md completo:

markdown
Copy code
# Pytube Video and Audio Downloader

Este es un sencillo script de Python que utiliza la biblioteca Pytube para descargar videos y audio de YouTube. El script te permite ingresar un enlace de YouTube y luego elegir si deseas descargar el video o solo el audio.

## Requisitos

- Python 3.x
- La biblioteca Pytube (`pip install pytube`)

## Uso

1. Ejecuta el script `youdownloader.py` en tu entorno de Python.

```bash
python youdownloader.py
```

2. El script te pedirá que ingreses el enlace del video de YouTube que deseas descargar.

3. Luego, el script te preguntará si deseas descargar el video o solo el audio:
   - Para descargar el audio, ingresa "1".
   - Para descargar el video, ingresa "2".
   - Para salir del programa, ingresa "3".

4. El script descargará el contenido seleccionado en la carpeta `./media` en tu directorio de trabajo actual.

## Notas
Los archivos descargados se guardan en las subcarpetas `./media/audio` y `./media/video`.
El archivo se guarda con el título del video como nombre de archivo.
El script se cierra automáticamente al descargar el archivo.

## Autor
Nombre: Toni García (@tonicodev)

## Contribuciones
¡Siéntete libre de contribuir a este proyecto y mejorar su funcionalidad!

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.