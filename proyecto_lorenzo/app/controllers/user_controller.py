from flask import Blueprint, render_template, request, redirect, url_for,current_app
from flask_bcrypt import Bcrypt
from flask import session

user_bp = Blueprint('user_bp', __name__)
bcrypt = Bcrypt()

# Login
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        connection =current_app.connection  # Obtén la conexión de la aplicación
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT contraseña FROM usuarios WHERE correo = %s", (correo,))
                result = cursor.fetchone()
                if result and bcrypt.check_password_hash(result['contraseña'], contraseña):
                    session['user_correo'] = correo  # Guarda el correo en la sesión
                    return redirect(url_for('user_bp.casomusica_modificado'))  # Cambia a tu página principal
                else:
                    return "inicio sesion fallida no tiene usuario creado"
        except Exception as e:
            return str(e)

    return render_template('login.html')


#  Registro
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    connection = current_app.connection
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        rol = request.form['rol']
        hashed_password = bcrypt.generate_password_hash(contraseña).decode('utf-8')

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuarios (nombre, correo, contraseña, rol) VALUES (%s, %s, %s, %s)",
                    (nombre, correo, hashed_password, rol)
                )
                connection.commit()
                return redirect(url_for('user_bp.login'))
        except Exception as e:
            return str(e)

    # Obtener roles
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, role_name FROM roles")
            roles = cursor.fetchall()
    except Exception as e:
        return str(e)

    return render_template('register.html', roles=roles)#
    
@user_bp.route('/casomusica_modificado')
def casomusica_modificado():
    return render_template('casomusica_modificado.html')
