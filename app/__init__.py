from flask import Flask
from flask_jw_extended import JWTManager

#importamos las configuraciones de la app

#manejo de las rutas con el blueprint


def create_app():
        app = Flask(
            __name__
            static_folder="static"
            template_folder="templates"

        )

    #cargamos las configuraciones 
    #
    #app.congig.from_object(config)

    #inicializamos la bd con la app

    #inicializamos el jwt 

    #registremos las rutas 

    #API auth

        with app.app_context():
                #inicializamos los modelos

                #creamos la bd

                return app