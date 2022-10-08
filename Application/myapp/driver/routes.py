
from flask import (Blueprint, request, render_template, redirect,
                    url_for, flash)
from myapp.models import User, Vehicle
from myapp import db
from flask_login import login_required, current_user
import os
from datetime import datetime

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
        driver_id_image = request.files["driver_id_image"]
        driver_license_image = request.files["driver_license_image"]
        driver_license_no = request.form.get("driver_license_no")
        driver_endorsed = request.form.get("license_endorsed")
        driver_license_renewal = request.form.get("renewal_date")
        cell_no = request.form.get("cell_no")
        family = request.form.get("family_member")
        
        # saving driver license image
        li_ext = driver_id_image.filename.split(".")[-1]
        li_img_name = f"{name}_{employee}_license_.{li_ext}"
        driver_license_image.save(
            os.path.join(os.getcwd(), "myapp","static", "drivers_images", li_img_name)
        )
        driver_license_image_str = "static/drivers_images/" + li_img_name
        
        # saving driver id image in driver image folder
        ext = driver_id_image.filename.split(".")[-1]
        img_name = f"{name}_{employee}_idCard_.{ext}"
        driver_id_image.save(
            os.path.join(os.getcwd(), "myapp","static", "drivers_images", img_name)
        )
        driver_id_image = "static/drivers_images/" + img_name
        
        # changing date string to actual date time
        print(f"date is: {driver_license_renewal}")
        dt_obj = datetime.strptime(driver_license_renewal, "%Y-%m-%d").date()
        print(type(dt_obj))
        # adding data to user model
        my_user = User(username=name, email=email,
                       password=password,employee_no=employee,
                       driver_license_image=driver_license_image_str,
                       id_no_image=driver_id_image,
                       fleet_no=fleet_no, milage=milage,
                       drivers_license_no=driver_license_no,
                       drivers_license_endorced=driver_endorsed,
                       drivers_license_renewal_date=dt_obj,
                       cell_no=cell_no, family_members=family)      
        db.session.add(my_user)
        db.session.commit()
        
        return redirect(url_for('Admin_DriverVehicle.drivers'))

    return render_template("admin/driver/add_driver.html",
                           dclass="router-link-active")


# Delete a driver
@Admin_DriverVehicle.route("/delete_driver/<string:driver_id>")
@login_required
def delete_driver(driver_id):
    if current_user.is_authenticated and current_user.is_admin:
        driver = User.query.get(driver_id)
        db.session.delete(driver)
        db.session.commit()
        return redirect(url_for('Admin_DriverVehicle.drivers'))


# edit a driver
@Admin_DriverVehicle.route("/edit_driver/<string:driver_id>", methods=["GET", "POST"])
@login_required
def edit_driver(driver_id):
    if current_user.is_authenticated and current_user.is_admin:
        if request.method == "POST":
            user = User.query.get(driver_id)
            
            email = request.form.get("email")
            password = request.form.get("password")
            if password=='':
                password = user.password
            name = request.form.get("full name")
            employee = request.form.get("employee")
            fleet_no = request.form.get("fleet")
            milage = request.form.get("milage")
            driver_id_image = request.files["driver_id_image"]
            driver_license_image = request.files["driver_license_image"]
            driver_license_no = request.form.get("driver_license_no")
            driver_endorsed = request.form.get("license_endorsed")
            driver_license_renewal = request.form.get("renewal_date")
            cell_no = request.form.get("cell_no")
            family = request.form.get("family_member")
            
            if driver_license_image.filename != '':
                # saving driver license image
                li_ext = driver_id_image.filename.split(".")[-1]
                li_img_name = f"{name}_{employee}_license_.{li_ext}"
                driver_license_image.save(
                    os.path.join(os.getcwd(), "myapp","static", "drivers_images", li_img_name)
                )
                driver_license_image_str = "static/drivers_images/" + li_img_name
                
            else:
                driver_license_image_str = user.driver_license_image
            
            if driver_id_image.filename != '':
                # saving driver id image in driver image folder
                ext = driver_id_image.filename.split(".")[-1]
                img_name = f"{name}_{employee}_idCard_.{ext}"
                driver_id_image.save(
                    os.path.join(os.getcwd(), "myapp","static", "drivers_images", img_name)
                )
                driver_id_image = "static/drivers_images/" + img_name
            else:
                driver_id_image = user.id_no_image
            
            # changing date string to actual date time
            dt_obj = datetime.strptime(driver_license_renewal, "%Y-%m-%d").date()

            # adding data to user model
            user.email = email
            user.password = password
            user.username = name
            user.employee_no = employee
            user.fleet_no = fleet_no
            user.milage = milage
            user.id_no_image = driver_id_image
            user.driver_license_image = driver_license_image_str
            user.driver_license_no = driver_license_no
            user.drivers_license_endorced = driver_endorsed
            user.drivers_license_renewal_date = dt_obj
            user.cell_no = cell_no
            user.family_members = family
            
            db.session.commit()
            return redirect(url_for('Admin_DriverVehicle.drivers'))
        else:
            driver = User.query.get(driver_id)
            return render_template("admin/driver/edit_driver.html",
                                   driver=driver)

@Admin_DriverVehicle.route("/vehicle",methods=["GET","POST"])
def vehicle():
    if request.method == "POST":
        actual = request.form.get("actual_contract_balance")
        interest_rate = request.form.get("interest_rate")
        take_on_Odo = request.form.get("Take_on_Odo")
        vehicle_manufacturer = request.form.get("vehicle_manufacturer")
        date_registration = request.form.get("date_of_first_registration")
        model = request.form.get("model")
        color = request.form.get("color")
        mobile_number = request.form.get("mobile_number")
        engine_no = request.form.get("engine_no")
        vin_no = request.form.get("vin_no")
        tank_capacity = request.form.get("tank_capacity")
        registration_no = request.form.get("registration_no")
        financer = request.form.get("financer")
        account_no = request.form.get("account_no")
        original_capital_balance = request.form.get("original_capital_balance")
        installment_amount = request.form.get("installment_amount")
        freuency_of_installment = request.form.get("freuency_of_installment")
        date_commenced = request.form.get("date_commenced")
        expiry_date = request.form.get("expiry_date")
        original_term = request.form.get("original_term")
        remaining_installments = request.form.get("remaining_installments")
        balloon_residual = request.form.get("balloon_residual")
        outstanding_capital_balance = request.form.get("outstanding_capital_balance")
        advance_amount = request.form.get("advance_amount")
        license_disk_expiry_date = request.form.get("license_disk_expiry_date")
        license_disk_renewal_reminder = request.form.get("license_disk_renewal_reminder")
        assign_to_a_driver = request.form.get('assign_to_a_driver')

        vh = Vehicle(
            registration_no=registration_no,
            financer = financer,
            account_no= account_no,
            original_capital_balance= original_capital_balance, 
            installment_amount= installment_amount,
            frequency_of_installment= freuency_of_installment,
            # date_commenced= date_commenced, 
            date_commenced= datetime.now(), 
            # expiry_date= expiry_date, 
            expiry_date= datetime.now(), 
            original_term= original_term, 
            remaining_installments= remaining_installments,
            # balloon_risidual= balloon_residual, 
            balloon_risidual= datetime.now(), 
            outstanding_capital_balance= outstanding_capital_balance,
            advance_amount= advance_amount, 
            actual_contract_balance= actual,
            interest_rate= interest_rate, 
            take_on_odo= take_on_Odo,
            vehicle_manufacturer= vehicle_manufacturer, 
            # date_of_first_registration= date_registration,
            date_of_first_registration= datetime.now(),
            model= model, color= color, 
            mobile_number= mobile_number,
            engine_no= engine_no, vin_no= vin_no, 
            tank_capacity= tank_capacity,
            # license_disk_expiry_date= license_disk_expiry_date,
            license_disk_expiry_date= datetime.now(),
            # license_disk_renewal_date= license_disk_renewal_reminder
            license_disk_renewal_date= datetime.now(),
            driver_id= assign_to_a_driver,
        )

        db.session.add(vh)
        db.session.commit()
        return redirect(url_for('Admin_DriverVehicle.vehicle_form'))

    driver = User.query.filter_by(is_admin=False).all()

    return render_template("admin/vehicle/vehicle_page.html",
                           vclass="router-link-active", driver= driver)


@Admin_DriverVehicle.route("/vehicle_form")
def vehicle_form():
    my_vehicle = Vehicle.query.all()
    return render_template('admin/vehicle/vehicle_form.html',
            my_vehicle = my_vehicle)