
# 📁 Python File Organizer

## 🌟 Descripción del Proyecto

Este es un script de automatización simple desarrollado en Python que permite **organizar y clasificar automáticamente todos los archivos** dentro de un directorio específico.

El script escanea el directorio raíz y mueve los archivos a subcarpetas dedicadas basadas en su extensión (`.jpg` a `/Images`, `.pdf` a `/Documents`, etc.).

---

## 🚀 Cómo Empezar

### Prerrequisitos

Este script utiliza únicamente módulos que vienen preinstalados con Python. No necesitas instalar librerías externas.

* **Python 3.x** instalado en tu sistema.

### Uso

Para utilizar el organizador, sigue estos pasos:

1.  **Define la Ruta:** Abre el archivo `file_organizer.py` y localiza la variable `Organizer_Path`.
2.  **Ajusta la Ruta:** Modifica el valor de esta variable para que apunte al **directorio que deseas organizar**.
    * *Ejemplo para Windows:* `Organizer_Path = r"D:\Users\Nacho\Descargas\ArchivosDesordenados"`
    * *(Nota: Se usa la 'r' de "raw string" para manejar correctamente las rutas de Windows.)*
3.  **Ejecuta el Script:** Abre tu terminal o consola, navega al directorio del proyecto y ejecuta:

    ```bash
    python file_organizer.py
    ```

El script imprimirá el progreso en la consola (creación de carpetas y movimiento de archivos) y, al finalizar, tu carpeta estará organizada.

---

## 📂 Estructura de Clasificación

El script utiliza el siguiente mapa para la clasificación (puedes modificarlo en el diccionario `FILES_TYPES`):

| Carpeta (Categoría) | Extensiones que Clasifica |
| :--- | :--- |
| **Images** | `.jpeg`, `.jpg`, `.png`, `.gif` |
| **Documents** | `.pdf`, `.docx`, `.txt`, `.xlsx` |
| **Videos** | `.mp4`, `.mov`, `.avi` |
| **Music** | `.mp3`, `.wav` |
| **Code** | `.py`, `.html`, `.css`, `.js` |
| **Others** | Cualquier archivo que no coincida con las categorías anteriores. |

---

## 🛠️ Tecnologías Usadas

* **Python 3.x**
* **Módulo `os`**: Para la interacción con el sistema operativo (listado de directorios y manipulación de rutas).
* **Módulo `shutil`**: Para operaciones de alto nivel como mover archivos.

<h1>Hola! 😁</h1>
<div>
  En este repositorio iré dejando todo tipos de protectos pequeños que haya logrado hacer, también me sirve para seguir aprendiendo constantemente y dejarlo acá como logros personales, soy nuevo en esto asi que recién estoy empezando.  😅
</div> <br>

<div>
  Si llegaste acá y deseas revisar lo que suba, sientene libre de hacerlo! ✌️ <br>
  Espero que también te sirva para aprender o darte ideas para tus propios proyectos.	😌  <br>
</div>

