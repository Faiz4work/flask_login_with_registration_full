from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from myapp.config import Config
from flask_admin import Admin
from flask_admin import expose, AdminIndexView
from flask_migrate import Migrate


login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message = "Please login to access Dashboard"
login_manager.login_message_category = "warning"
db = SQLAlchemy()

migrate = Migrate()

# admin index view
class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):

        from myapp.models import User
        users = User.query.filter_by(is_admin=False).all()
        return self.render('admin/index.html', users=users)
admin = Admin(template_mode="bootstrap4", 
                index_view=MyHomeView())

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)
    
    admin.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from myapp.user.routes import user
    app.register_blueprint(user)
    
    from myapp.driver.routes import Admin_DriverVehicle
    app.register_blueprint(Admin_DriverVehicle)
    
    # importing admin blueprint
    from myapp.admin_bp import admin_bp
    app.register_blueprint(admin_bp)

    from myapp.driver_forms.routes import driver_forms
    app.register_blueprint(driver_forms)


    return app