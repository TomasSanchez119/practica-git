# Sistema de Gestión de Álbumes y Canciones

## Descripción

Este sistema permite gestionar álbumes musicales y sus canciones correspondientes. Los usuarios pueden crear álbumes, agregar canciones a los álbumes, editar y eliminar tanto álbumes como canciones.

## Características

- ✅ Crear nuevos álbumes
- ✅ Agregar canciones a álbumes específicos
- ✅ Editar información de canciones
- ✅ Eliminar álbumes y canciones
- ✅ Interfaz moderna con estética consistente
- ✅ Diseño responsivo

## Estructura de la Base de Datos

### Tabla `albumes`
- `id_album` (INT, AUTO_INCREMENT, PRIMARY KEY)
- `nombre` (VARCHAR(100))
- `artista` (VARCHAR(30))
- `año` (INT(5))
- `id_usuario` (INT(11), FOREIGN KEY)

### Tabla `musica`
- `id_musica` (INT, AUTO_INCREMENT, PRIMARY KEY)
- `titulo` (VARCHAR(100))
- `genero` (VARCHAR(50))
- `url` (VARCHAR(200))

### Tabla `albumes_musica`
- `id_playlist` (INT, FOREIGN KEY a albumes.id_album)
- `id_musica` (INT, FOREIGN KEY a musica.id_musica)

## Instalación y Configuración

### 1. Requisitos Previos
- Python 3.7+
- MySQL/MariaDB
- pip

### 2. Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### 3. Configuración de la Base de Datos
1. Crear la base de datos `lorenzopenso`
2. Importar el archivo `lorenzopenso.sql`
3. Verificar la configuración en `config.py`

### 4. Verificar la Conexión
```bash
python test_database.py
```

### 5. Ejecutar la Aplicación
```bash
python run.py
```

## Uso del Sistema

### Rutas Disponibles

#### Gestión de Álbumes
- `GET /GestionarM` - Listar todos los álbumes
- `GET /GestionarM/NuevoAlbum` - Formulario para crear nuevo álbum
- `POST /GestionarM/NuevoAlbum` - Crear nuevo álbum
- `GET /GestionarM/Ver/<id_album>` - Ver álbum específico
- `GET /GestionarM/EliminarAlbum/<id_album>` - Eliminar álbum

#### Gestión de Canciones
- `GET /GestionarM/NuevaCancion/<id_album>` - Formulario para agregar canción
- `POST /GestionarM/NuevaCancion/<id_album>` - Agregar canción al álbum
- `GET /GestionarM/Modificar/<id_cancion>` - Formulario para editar canción
- `POST /GestionarM/Modificar/<id_cancion>` - Actualizar canción
- `GET /GestionarM/Eliminar/<id_cancion>` - Eliminar canción

### Flujo de Trabajo

1. **Crear un Álbum**
   - Ir a `/GestionarM`
   - Hacer clic en "Nuevo Álbum"
   - Completar el formulario con nombre, artista y año
   - Guardar

2. **Agregar Canciones**
   - Desde la lista de álbumes, hacer clic en "Ver Álbum"
   - Hacer clic en "Agregar Canción"
   - Completar el formulario con título, género y URL (opcional)
   - Guardar

3. **Editar Canciones**
   - Desde la vista del álbum, hacer clic en "Editar"
   - Modificar la información
   - Guardar cambios

4. **Eliminar Elementos**
   - Usar los botones "Eliminar" correspondientes
   - Confirmar la acción

## Estética y Diseño

El sistema utiliza:
- **Color principal**: `#212529` (gris oscuro)
- **Color de acento**: `#78C5EF` (azul claro)
- **Bootstrap 5** para el diseño responsivo
- **Iconos de Bootstrap** para mejorar la UX
- **Efectos hover** y transiciones suaves

## Archivos Principales

### Controladores
- `app/controllers/GestionarM.py` - Lógica de gestión de álbumes y canciones

### Vistas
- `templates/albumes.html` - Lista de álbumes
- `templates/nuevo_album.html` - Crear álbum
- `templates/ver_album.html` - Ver álbum específico
- `templates/nueva_cancion.html` - Agregar canción
- `templates/editar_cancion.html` - Editar canción

### Configuración
- `config.py` - Configuración de la base de datos
- `lorenzopenso.sql` - Estructura de la base de datos

## Solución de Problemas

### Error de Conexión a la Base de Datos
1. Verificar que MySQL esté ejecutándose
2. Comprobar las credenciales en `config.py`
3. Asegurar que la base de datos `lorenzopenso` existe

### Error de Importación
1. Verificar que todas las dependencias estén instaladas
2. Ejecutar `pip install -r requirements.txt`

### Error de Rutas
1. Verificar que el blueprint esté registrado en `app/__init__.py`
2. Comprobar que las rutas estén correctamente definidas

## Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crear una rama para tu feature
3. Hacer los cambios necesarios
4. Crear un pull request

## Licencia

Este proyecto está bajo la licencia MIT. 