from flask import Flask as Fl

def create_app():
    app = Fl(__name__)
    app.config['SECRET_KEY'] = 'niggawompwomp1234'

    from .views import views
    from .auth import auth

    #app.register_blueprint(views, url_prefix='/Home')
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
