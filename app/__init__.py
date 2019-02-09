import os
from flask import Flask
def create_app(test_config=None):
    #the application factory function
    #create and configure
    app = Flask(__name__, instance_relative_config=True)
    #creates the Flask instance
    #__name__ is the name of the current Python module,
    # it tells location and set up some paths
    app.config.from_mapping(
        SECRET_KEY='dev'
        #DB will be included here
    )

    if test_config is None:
        #load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    
    else:
        #load the test config if passed in
        app.config.from_mapping(test_config)
    
    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Test if it can run a hello world
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    #Import and register the blueprint 
    #from the factory using app.register_blueprint()
    from .api.v1 import party
    app.register_blueprint(party.bp)


    return app