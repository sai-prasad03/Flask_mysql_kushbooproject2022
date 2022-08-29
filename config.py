class Config(object):
    """"
    common configuration
    """
    SECRET_KEY='AKSHAY1234'
    ##SQLALCHEMY_DATABASE_URI='<use_database>://username:password@<ip>/<database_name>
    SQLALCHEMY_DATABASE_URI ='mysql://root:root@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATION=False

#pip install Flask-SQLAlchemy
#pip install mysqlclint
class Development_config(Config):
    """"
    development configuration
    """
    DEBUG=True
    SQLALCHEMY_ECHO=True

class Testing_config(Config):
    """
    testing configuration
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flask_test_db'
    SQLALCHEMY_TRACK_MODIFICATION = False

class Production_config(Config):
    """
    Production configuration
    """
    DEBUG=False

app_config ={
    'development':Development_config,
    'testing':Testing_config,
    'production':Production_config
}
