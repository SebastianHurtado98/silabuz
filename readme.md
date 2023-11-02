# Music API Project

Este es el proyecto Music API, que es una API RESTful para gestionar artistas, álbumes y canciones.

## Configuración del proyecto

Para ejecutar este proyecto, sigue estos pasos.

### Pre-requisitos

Antes de comenzar, asegúrate de tener instalado Python en tu sistema. Este proyecto usa Python 3.

Es recomendable también que uses `virtualenv` para crear un entorno virtual para el proyecto.

### Instalación

1. Clona este repositorio o descarga el código fuente.

2. Crea un entorno virtual dentro del directorio principal del proyecto:

    ```bash
    virtualenv .venv
    ```

3. Activa el entorno virtual:

    ```bash
    source .venv/bin/activate
    ```

4. Navega al directorio del proyecto `music_app`:

    ```bash
    cd music_app
    ```

5. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

### Configuración de la base de datos

Ejecuta las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```

### Ejecutar el servidor

Inicia el servidor de desarrollo:


```bash
python manage.py runserver
```

### Documentación

Accede a la documentación: [Aquí](http://127.0.0.1:8000/swagger/).