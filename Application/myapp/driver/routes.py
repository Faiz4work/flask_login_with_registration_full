from flask import (Blueprint, request, render_template, redirect,
                    url_for, flash)
from myapp.models import User, Vehicle
from myapp import db
from flask_login import (login_user, logout_user, 
                            login_required, current_user)


Admin_DriverVehicle = Blueprint("Admin_DriverVehicle", __name__)

@Admin_DriverVehicle.route("/drivers")
def drivers():
    drivers = User.query.filter_by(is_admin=False).all()
    return render_template("admin/driver/drivers_info.html",
                           dclass="router-link-active", drivers=drivers)



# add driver form route
@Admin_DriverVehicle.route("/add_driver", methods=["GET", "POST"])
def add_driver():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("full name")
        employee = request.form.get("employee")
        fleet_no = request.form.get("fleet")
        milage = request.form.get("milage")
        image = request.files["image"]
        driver_license = request.form.get("driver_license")
        print(driver_license)

        driver_endorsed = request.form.get("license_endorsed")
        print(driver_endorsed)

        driver_license_renewal = request.form.get("renewal_date")
        print(driver_license_renewal)

        cell_no = request.form.get("cell_no")
        print(cell_no)

        family = request.form.get("family_member")
        
        # adding data to user model

        my_user = User(username=name, email=email,
                       password=password,employee_no=employee,
                       fleet_no=fleet_no, milage=milage,
                       drivers_license_no=driver_license,
                       drivers_license_endorced=driver_endorsed,
                       cell_no=cell_no, family_members=family)      
        db.session.add(my_user)
        db.session.commit()


    return render_template("admin/driver/add_driver.html",
                           dclass="router-link-active")
    

@Admin_DriverVehicle.route("/vehicle",methods=["GET","POST"])
def vehicle():
    if request.method == "POST":
        actual = request.form.get("actual")
        interest_rate = request.form.get("interest_rate")
        take_on_Odo = request.form.get("take_on_Odo")
        vehicle_manufacturer = request.form.get("vehicle_manufacturer")
        date_registration = request.form.get("date_registration")
        model = request.form.get("model")
        colour = request.form.get("colour")
        mobile_no = request.form.get("mobile_no")
        engine_no = request.form.get("engine_no")
        vin_no = request.form.get("vin_no")
        tank_capacity = request.form.get("tank_capacity")


    my_user2 = User(actual=actual, interest_rate=interest_rate,
                   take_on_Odo=take_on_Odo, vehicle_manufacturer=vehicle_manufacturer,
                   date_registration=date_registration, model=model, 
                   colour=colour, mobile_no=mobile_no, engine_no=engine_no, 
                   vin_no=vin_no, tank_capacity=tank_capacity )

    db.session.add(my_user2)
    db.session.commit()

    return render_template("admin/vehicle/vehicle_page.html",
                           vclass="router-link-active")