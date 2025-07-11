from flask import Flask
import pymysql.cursors
from config import Config


def create_app():
    app = Flask(__name__, template_folder='../templates',static_folder='../static')
    app.config.from_object(Config)


    # Configuración de base de datos
 # Initialize database connection
    connection= pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=pymysql.cursors.DictCursor
    )

     

    # Blueprints
    from app.controllers.home_controller import home_bp
    from app.controllers.user_controller import user_bp
    from app.controllers.GestionarM import GestionarM_bp 

    app.register_blueprint(user_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(GestionarM_bp)

    app.connection = connection

    return app
