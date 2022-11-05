from sqlalchemy import func
from myapp import admin
from myapp.models import (User, Vehicle, VehicleExpense,
            FleetIncidentReporting, FleetNcIncidentReporting)
from flask_admin.contrib.sqla import ModelView
from myapp import db
from flask_admin import BaseView, expose
from flask_login import current_user
from flask_admin.menu import MenuLink
from flask import request, flash, redirect, url_for
from datetime import datetime
import os



class UserView(ModelView):
    # hiding list columns to view them in user page
    column_exclude_list = ['milage', 'cell_no', 'registration_no',
                           'fleet_no', 'driver_license_image', 'id_no_image',
                           'drivers_license_no', 'drivers_license_endorced',
                           'drivers_license_renewal_date', 'family_members']
    # hiding form columns for editing the user
    form_excluded_columns = ['milage', 'cell_no', 'registration_no',
                           'fleet_no', 'driver_license_image', 'id_no_image',
                           'drivers_license_no', 'drivers_license_endorced',
                           'drivers_license_renewal_date', 'family_members']
    
    def is_accessible(self):
        if current_user.is_authenticated and current_user.is_admin:
            return True
        else:
            return False
    
    # adding a function to show only admins
    def get_query(self):
        return self.session.query(self.model).filter(self.model.is_admin==True)
    
    # adding a function to get count of users
    # def get_query_count(self):
    #     return self.session.query(func.count("*")).filter(self.model.is_admin==True)
    
    
admin.add_view(UserView(User, db.session, endpoint="Users"))

# adding logout link
admin.add_link(MenuLink(name="Logout", url="/logout"))





# Adding drivers list in admin page
class DriversList(BaseView):
    @expose("/")
    def index(self):
        drivers = User.query.filter_by(is_admin=False).all()
        return self.render("admin/drivers_list.html", drivers=drivers)

admin.add_view(DriversList(name="Drivers List", endpoint="drivers_list"))


# Adding vehicle model in view
admin.add_view(ModelView(Vehicle, db.session))


# adding drivers form
class DriverForm(BaseView):
    @expose("/", methods=["GET", "POST"])
    def index(self):
        if request.method == "POST":
            registration_no = request.form.get("registration_no")
            fleet_no = request.form.get("fleet")
            milage = request.form.get("milage")
            driver_license_image = request.files["driver_license"]
            username = request.form.get("username")
            id_no_image = request.files["id_no"]
            drivers_license_no = request.form.get("drivers_license_no")
            license_endorsed = request.form.get("license_endorsed")
            license_renewal = datetime.strptime(request.form.get("license_renewal"), "%Y-%m-%d")
            cell_no = request.form.get("cell_no")
            family_members = request.form.get("family_member")
            email = request.form.get("email")
            password = request.form.get("password")
            
            image_upload_path = os.path.join(os.getcwd(), "myapp", "static", "drivers_images")
            
            # saving driver license image
            dfilename = driver_license_image.filename
            new_dfilename = f"{registration_no}_{username}_{dfilename}"
            driver_license_image_name = new_dfilename
            driver_license_image.save(os.path.join(image_upload_path, driver_license_image_name))
            driver_license_image_full_path = "static/drivers_images/" + driver_license_image_name
            
            # saving driver id no
            idfilename = id_no_image.filename
            new_id_filename = f"{registration_no}_id_no_image_{idfilename}"
            id_no_image_name = new_id_filename
            id_no_image.save(os.path.join(image_upload_path, id_no_image_name))
            id_no_image_full_path = "static/drivers_images/" + id_no_image_name
            
            
            user = User(username=username, email=email, password=password,
                        registration_no=registration_no, fleet_no=fleet_no,
                        milage=milage, driver_license_image=driver_license_image_full_path,
                        id_no_image=id_no_image_full_path, drivers_license_no=drivers_license_no,
                        drivers_license_endorced=license_endorsed,
                        drivers_license_renewal_date=license_renewal,
                        cell_no=cell_no, family_members=family_members)
            db.session.add(user)
            # try:
            db.session.commit()
            flash(f"{username} has been added.", "danger")
            return redirect(url_for("drivers_list.index")) 
            # except Exception as e:
            #     print(f"Exception caught as: {e}")
            #     db.session.rollback()
        return self.render("admin/driver_addition_form.html")
    
admin.add_view(DriverForm(name="", endpoint="drivers_form"))


# Single Driver's all expenses page
class DriverExpensePage(BaseView):
    @expose("/")
    def index(self):
        did = request.args.get("id")
        vehicle_expenses = VehicleExpense.query.filter_by(driver_id=did).all()
        incident_expenses = FleetIncidentReporting.query.filter_by(driver_id=did).all()
        nc_incident = FleetNcIncidentReporting.query.filter_by(driver_id=did).all()
        return self.render("admin/driver/expense_page.html", 
                           vehicle_expenses=vehicle_expenses,
                           incident_expenses=incident_expenses,
                           nc_incident=nc_incident,
                           dashboard="router-link-active")

admin.add_view(DriverExpensePage(name="Driver Expense Page", endpoint="driver_expense"))
