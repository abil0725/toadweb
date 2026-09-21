import os

class config:
    SQLALCHEMY_DATABASE:URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://Jroot_user:Jroot_pass@db:3306/RIUL_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECREY_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "super-clave-secret"
    )
    #3600 segundos = 1 hora
    JWT_ACCES_TOKEN_EXPIRES = 3600