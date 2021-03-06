"""
    Author : Thibault Chenevière
    Date : 26/09/2021
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.firstSite'
    app.config['SECRET_KEY'] = '29FTh4Swfr3DuMlNRcQcZxCk7IFBMooP'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from py.site.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from py.site.authBP import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from py.site.mainBP import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from py.site.adminBP import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from py.site.profileBP import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=1)


