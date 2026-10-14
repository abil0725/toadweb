from flask import Flask
from flask_jwt_extended import JWTManager

#importamos las configuraciones de la app
from app.config import config
from app.extencions import db
#manejo de las rutas con el blueprint


def create_app():
        app = Flask(
            __name__,
            static_folder="static",
            template_folder="templates",
        )

    #cargamos las configuraciones 
    #
        app.config.from_object(config)

    #inicializamos la bd con la app
        db.init_app(app)

    #inicializamos el jwt 
        JWTManager(app) 
    #registremos las rutas 

    #API auth

        with app.app_context():
                #inicializamos los modelos

                #creamos la bd

                return app