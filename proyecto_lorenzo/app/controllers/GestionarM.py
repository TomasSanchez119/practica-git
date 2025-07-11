from flask import Blueprint, render_template, request, redirect, url_for, session
import pymysql
from config import Config

GestionarM_bp = Blueprint('GestionarM_bp', __name__)

# Función para conectar a la base de datos
def get_connection():
    return pymysql.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor
    )

@GestionarM_bp.route('/GestionarM')
def listar_albumes():
    connection = get_connection()
    with connection.cursor() as cursor:
        # Obtener todos los álbumes
        cursor.execute("SELECT * FROM albumes ORDER BY nombre")
        albumes = cursor.fetchall()
    connection.close()
    return render_template('albumes.html', albumes=albumes)

@GestionarM_bp.route('/GestionarM/Ver/<int:id_album>')
def ver_album(id_album):
    connection = get_connection()
    with connection.cursor() as cursor:
        # Obtener información del álbum
        cursor.execute("SELECT * FROM albumes WHERE id_album = %s", (id_album,))
        album = cursor.fetchone()
        
        # Obtener canciones del álbum
        cursor.execute("""
            SELECT m.* FROM musica m 
            INNER JOIN albumes_musica am ON m.id_musica = am.id_musica 
            WHERE am.id_playlist = %s
        """, (id_album,))
        canciones = cursor.fetchall()
    connection.close()
    return render_template('ver_album.html', album=album, canciones=canciones)

@GestionarM_bp.route('/GestionarM/NuevoAlbum', methods=['GET', 'POST'])
def nuevo_album():
    if request.method == 'POST':
        nombre = request.form['nombre']
        artista = request.form['artista']
        año = request.form['año']
        id_usuario = session.get('user_id', 1)  # Por defecto usuario 1 si no hay sesión

        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO albumes (nombre, artista, año, id_usuario)
                VALUES (%s, %s, %s, %s)
            """, (nombre, artista, año, id_usuario))
            connection.commit()
        connection.close()
        return redirect(url_for('GestionarM_bp.listar_albumes'))

    return render_template('nuevo_album.html')

@GestionarM_bp.route('/GestionarM/NuevaCancion/<int:id_album>', methods=['GET', 'POST'])
def nueva_cancion(id_album):
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        url = request.form['url']

        connection = get_connection()
        with connection.cursor() as cursor:
            # Insertar la canción
            cursor.execute("""
                INSERT INTO musica (titulo, genero, url)
                VALUES (%s, %s, %s)
            """, (titulo, genero, url))
            
            # Obtener el ID de la canción insertada
            id_musica = cursor.lastrowid
            
            # Relacionar la canción con el álbum
            cursor.execute("""
                INSERT INTO albumes_musica (id_playlist, id_musica)
                VALUES (%s, %s)
            """, (id_album, id_musica))
            
            connection.commit()
        connection.close()
        return redirect(url_for('GestionarM_bp.ver_album', id_album=id_album))

    # Obtener información del álbum para mostrar en la vista
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM albumes WHERE id_album = %s", (id_album,))
        album = cursor.fetchone()
    connection.close()
    
    return render_template('nueva_cancion.html', album=album)

@GestionarM_bp.route('/GestionarM/Modificar/<int:id>', methods=['GET', 'POST'])
def editar_cancion(id):
    connection = get_connection()
    with connection.cursor() as cursor:
        if request.method == 'POST':
            titulo = request.form['titulo']
            genero = request.form['genero']
            url = request.form['url']

            cursor.execute("""
                UPDATE musica SET titulo=%s, genero=%s, url=%s
                WHERE id_musica=%s
            """, (titulo, genero, url, id))
            connection.commit()
            connection.close()
            
            # Redirigir de vuelta al álbum
            return redirect(url_for('GestionarM_bp.listar_albumes'))
        
        cursor.execute("SELECT * FROM musica WHERE id_musica = %s", (id,))
        cancion = cursor.fetchone()
    connection.close()
    return render_template('editar_cancion.html', cancion=cancion)

@GestionarM_bp.route('/GestionarM/Eliminar/<int:id>')
def eliminar_cancion(id):
    connection = get_connection()
    with connection.cursor() as cursor:
        # Obtener el álbum antes de eliminar para redirigir
        cursor.execute("""
            SELECT am.id_playlist FROM albumes_musica am 
            WHERE am.id_musica = %s
        """, (id,))
        album_rel = cursor.fetchone()
        
        if album_rel:
            id_album = album_rel['id_playlist']
            # Eliminar la relación primero
            cursor.execute("DELETE FROM albumes_musica WHERE id_musica = %s", (id,))
            # Luego eliminar la canción
            cursor.execute("DELETE FROM musica WHERE id_musica = %s", (id,))
            connection.commit()
            connection.close()
            return redirect(url_for('GestionarM_bp.ver_album', id_album=id_album))
        else:
            connection.close()
            return redirect(url_for('GestionarM_bp.listar_albumes'))

@GestionarM_bp.route('/GestionarM/EliminarAlbum/<int:id_album>')
def eliminar_album(id_album):
    connection = get_connection()
    with connection.cursor() as cursor:
        # Obtener todas las canciones del álbum
        cursor.execute("""
            SELECT id_musica FROM albumes_musica 
            WHERE id_playlist = %s
        """, (id_album,))
        canciones = cursor.fetchall()
        
        # Eliminar las relaciones primero
        cursor.execute("DELETE FROM albumes_musica WHERE id_playlist = %s", (id_album,))
        
        # Eliminar las canciones
        for cancion in canciones:
            cursor.execute("DELETE FROM musica WHERE id_musica = %s", (cancion['id_musica'],))
        
        # Eliminar el álbum
        cursor.execute("DELETE FROM albumes WHERE id_album = %s", (id_album,))
        
        connection.commit()
    connection.close()
    return redirect(url_for('GestionarM_bp.listar_albumes'))
