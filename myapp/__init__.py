from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from myapp.config import Config
from flask_admin import Admin
from flask_admin import expose, AdminIndexView
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy import MetaData

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message = "Please login to access Dashboard"
login_manager.login_message_category = "warning"
metadata = MetaData(
    naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
    }
)

db=SQLAlchemy(metadata=metadata)

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


# change date string to python datetime object
def change_to_datetime(dstring):
    year = dstring.split("-")[0]
    month = dstring.split("-")[1]
    day = dstring.split("-")[2]
    
    return datetime(year=int(year), month=int(month), day=int(day))
    
    