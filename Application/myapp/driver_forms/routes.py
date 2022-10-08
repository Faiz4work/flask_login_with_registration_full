from flask import Blueprint, render_template, request
from myapp.models import FleetCard, MaintenancesTyres, FleetIncidentReporting, FleetNcIncidentReporting, fleet_inspection_card_form
from myapp import db
from datetime import datetime
from flask_login import current_user

driver_forms = Blueprint("driver_forms", __name__)

def convert_str_to_datetime_obj(date_str):
    dlist = date_str.split("-")
    myyear = dlist[0]
    mymonth = int(dlist[1])
    myday = int(dlist[2])
    final_date = datetime(year=int(myyear), month=mymonth,
        day=myday)
    
    return final_date

@driver_forms.route("/fleet_card_form",methods=["POST","GET"])
def fleet_card_form():
    if request.method=="POST":
        registration_no = request.form.get("registration_no")
        driver_name = request.form.get("driver_name")
        take_on_odo =request.form.get("take_on_odo")
        vehicle_manufacturer = request.form.get("vehicle_manufacturer")
        date_of_first_registration = request.form.get("date_of_first_registration")
        model_name = request.form.get("model_name")
        color_name = request.form.get("color_name")
        mobile_no = request.form.get("mobile_no")
        engine_no = request.form.get("engine_no")
        vin_no = request.form.get("vin_no")
        tank_capacity = request.form.get("tank_capacity")
        employee_no = request.form.get("employee_no")

        my_date_of_first_registration = convert_str_to_datetime_obj(date_of_first_registration)

        card = FleetCard(
            registration_no = registration_no,
            driver = driver_name,
            take_on_odo = take_on_odo,
            vehicle_manufacturer = vehicle_manufacturer,
            # date_of_first_registration = my_date_of_first_registration,
            date_of_first_registration = my_date_of_first_registration,

            model = model_name,
            color = color_name,
            mobile_number = mobile_no,
            engine_no = engine_no,
            vin_no = vin_no,
            tank_capacity = tank_capacity,
            employee_no = employee_no,
            driver_id = current_user.id,
        )

        db.session.add(card)
        db.session.commit()
    

    return render_template("driver_forms/fleet_card_order_form.html",
                fleet_card_class="router-link-active")


@driver_forms.route("/maintenance_card_form",methods=["POST","GET"])
def maintenance_card_form():
    if request.method=="POST":
        Driver_name = request.form.get("driver_name")
        reg_num = request.form.get("reg_num")
        yr_mth = request.form.get("yr_mth")
        make = request.form.get("make")
        Model = request.form.get("Model")
        Fuel_Value = request.form.get("Fuel_Value")
        Km_Travelled = request.form.get("Km_Travelled")
        oil_value = request.form.get("Oil_Value")
        km = request.form.get("km")
        Repair_and_Maint = request.form.get("Repair_and_Maint")
        Maintenance_Plan = request.form.get("Maintenance_Plan")

        maintenance_expiry_date = request.form.get("maintenance_expiry_date")

        Type_of_Service = request.form.get("Type_of_Service")
        Service_Intervals = request.form.get("Service_Intervals")
        Tyre_Value = request.form.get("Tyre_Value")
        Accident_Value = request.form.get("Accident_Value")
        Accident_Incident = request.form.get("Accident_Incident")
        Other_Value = request.form.get("Other_Value")
        Description = request.form.get("Description")
        Toll_Value = request.form.get("Toll_Value")

        tyres = MaintenancesTyres(
            driver = Driver_name,
            reg_num = reg_num,
            yr_mth = yr_mth,
            make = make,
            model = Model,
            fuel_value = Fuel_Value,
            km_travelled = Km_Travelled,
            oil_value = oil_value,
            km = km,
            repair_and_maint = Repair_and_Maint,
            maintenance_plan = Maintenance_Plan,

            # maintenance_expiry_year_month_km_date = datetime.now(maintenance_expiry_date),
            maintenance_expiry_year_month_km_date = convert_str_to_datetime_obj(maintenance_expiry_date),

            type_of_service = Type_of_Service,
            service_intervals = Service_Intervals,
            tyre_value = Tyre_Value,
            accident_value = Accident_Value,
            accident_incident = Accident_Incident,
            other_value = Other_Value,
            description = Description,
            toll_value = Toll_Value,
        )

        db.session.add(tyres)
        db.session.commit()

    

    return render_template("driver_forms/maintenance.html",
            maintanance_card_class="router-link-active")


@driver_forms.route("/fleet_incident_card_form",methods=["POST","GET"])
def fleet_incident_reporting_form():
    if request.method=="POST":
        driver = request.form.get("driver_name")
        id_number_1 = request.form.get("id_number")
        license_no_1 = request.form.get("License")
        date_issued_1 = request.form.get("Date Issued")
        code_1 = request.form.get("Code")
        endorsed_1 = request.form.get("endorsed")
        do_you_have_your_own_insurance = request.form.get("do_you_have")
        details_of_your_insurance = request.form.get("details")
        details_of_previous_accidents = request.form.get("details_2")
        registration_no_1 = request.form.get("Registration")
        milage = request.form.get("milage")
        make_1 = request.form.get("make")
        model_1 = request.form.get("model")
        reason_for_passenger_in_vehicle = request.form.get("details_3")
        is_the_passenger_a_employee = request.form.get("passenger_2")
        name_surname_of_passenger = request.form.get("name")
        id_no_attach_copy_of_id = request.form.get("number")
        address_1 = request.form.get("address")
        details_of_injury_is = request.form.get("details")
        names_and_surname_of_driver = request.form.get("full_name")
        contact_details = request.form.get("contact")
        id_number_2 = request.form.get("id_no")
        license_no_2 = request.form.get("license_2")
        date_issued_2 = request.form.get("date_issued")
        code = request.form.get("Code_2")
        endorsed = request.form.get("endorsed_2")
        address_2 = request.form.get("address")
        company_name = request.form.get("company")
        company_address = request.form.get("company address")
        contact_person = request.form.get("contact_person")
        telephone_no = request.form.get("telephone_no")
        email_address = request.form.get("email_2")
        registration_no_2 = request.form.get("registration_2")
        colour_1 = request.form.get("colour_2")
        make_2 = request.form.get("make_2")
        model_2 = request.form.get("model_2")
        registration_no_3 = request.form.get("registration_no_3")
        colour_2 = request.form.get("colour_2")
        make_3 = request.form.get("make_3")
        model_3 = request.form.get("model_3")
        details_of = request.form.get("details_of")
        saps_case_no = request.form.get("saps")
        take_photo_1 = request.files['file']
        take_photo_2 = request.files['file_2']
        manager_1 = request.form.get("manager")
        date_1 = request.form.get("date")
        time_1 = request.form.get("time")
        manager_2 = request.form.get("manager_2")
        date_2 = request.form.get("date_2")
        time_2 = request.form.get("time_2")


        reporting = FleetIncidentReporting(
            driver = driver,
            id_number_1 = id_number_1,
            license_no_1 = license_no_1,

            # date_issued_1 = date_issued_1,
            driver_licencse_date_issued_1 = convert_str_to_datetime_obj(date_issued_1),

            code_1 = code_1,
            endorsed_1 = endorsed_1,
            do_you_have_your_own_insurance = do_you_have_your_own_insurance,
            details_of_your_insurance =  details_of_your_insurance,
            details_of_previous_accidents = details_of_previous_accidents,
            registration_no_1 = registration_no_1,
            milage = milage,
            make_1 = make_1,
            model_1 = model_1,
            reason_for_passenger_in_vehicle = reason_for_passenger_in_vehicle,
            is_the_passenger_a_employee = is_the_passenger_a_employee,
            name_surname_of_passenger = name_surname_of_passenger,
            id_no_attach_copy_of_id = id_no_attach_copy_of_id,
            address_1 = address_1,
            details_of_injury_is = details_of_injury_is,
            names_and_surname_of_driver = names_and_surname_of_driver,
            contact_details = contact_details,
            id_number_2 = id_number_2,
            license_no_2 = license_no_2,

            # date_issued = date_issued,
            driver_license_date_issued_2 = convert_str_to_datetime_obj(date_issued_2),

            code = code,
            endorsed = endorsed,
            address_2 = address_2,
            company_name = company_name,
            company_address = company_address,
            contact_person = contact_person,
            telephone_no = telephone_no,
            email_address = email_address,
            registration_no_2 = registration_no_2,
            colour_1 = colour_1,
            make_2 = make_2,
            model_2 = model_2,
            registration_no_3 = registration_no_3, 
            colour_2 = colour_2,
            make_3 = make_3,
            model_3 = model_3,
            details_of = details_of,
            saps_case_no = saps_case_no,
            take_photo_1 = 'take_photo_1',
            take_photo_2 = 'take_photo_2',
            manager_1 = manager_1,
            # date_1 = date_1,
            reporting_date_1 = convert_str_to_datetime_obj(date_1),
            time_1 = time_1,
            manager_2 = manager_2,
            # date_2 = date_2,
            reporting_date_2 = convert_str_to_datetime_obj(date_2),
            time_2 = time_2,
        )

        db.session.add(reporting)
        db.session.commit()

    return render_template('driver_forms/fleet_incident_card_form.html',
                fleet_incident_card_class="router-link-active")


@driver_forms.route("/fleet_N.C_incident_card_form",methods=["POST","GET"])
def fleet_N_incident_reporting_form():
    if request.method=="POST":
        registration_no = request.form.get("registration_no")
        vin = request.form.get("vin")
        make = request.form.get("make")
        vehicle_manufacturer = request.form.get("vehicle_manufacturer")
        License = request.form.get("License")
        date_issued = request.form.get("date_issued")
        code = request.form.get("code")
        endorsed = request.form.get("endorsed")
        License_2 = request.form.get("License_2")
        date_issued_2 = request.form.get("date_issued_2")
        Code_2 = request.form.get("Code_2")
        endorsed_2 = request.form.get("endorsed_2")
        demage = request.form.get("demage")
        demage_2 = request.form.get("demage_2")
        yes_no = request.form.get("yes_no")
        manager = request.form.get("manager")
        date = request.form.get("date")
        time = request.form.get("time")
        yes_no_2 = request.form.get("yes_no_2")
        manager_2 = request.form.get("manager_2")
        date_2 = request.form.get("date_2")
        time_2 = request.form.get("time_2")


        NC= FleetNcIncidentReporting(
            registration_no = registration_no,
            vin = vin,
            make = make,
            vehicle_manufacturer = vehicle_manufacturer,
            License = License,
            # date_issued = date_issued,
            driver_licence_date_issued = convert_str_to_datetime_obj(date_issued),

            code = code,
            endorsed = endorsed,
            License_2 = License_2,
            # date_issued_2 = date_issued_2,
            driver_licence_date_issued_2 = convert_str_to_datetime_obj(date_issued_2),

            Code_2 = Code_2,
            endorsed_2 = endorsed_2,
            demage = demage,
            demage_2 = demage_2,
            yes_no = yes_no,
            manager = manager,
            # date = date,
            reporting_date = convert_str_to_datetime_obj(date),

            time = time,
            yes_no_2 = yes_no_2,
            manager_2 = manager_2,
            # date_2 = date_2,
            reporting_date_2 = convert_str_to_datetime_obj(date_2),
            time_2 = time_2,
        )
        
        db.session.add(NC)
        db.session.commit()
        

    
    return render_template('driver_forms/fleet_N.C_incident_reporting_form.html',
                nc_card_class="router-link-active")


@driver_forms.route("/fleet_inspection_card_form",methods=["POST","GET"])
def fleet_inspection_reporting_form():
    if request.method=="POST":
        date_1 = request.form.get("date_1")
        time_1 = request.form.get("time_1")
        registration_1 = request.form.get("registration_1")
        fleet = request.form.get("fleet")
        milage_1 = request.form.get("milage_1")
        name = request.form.get("name")
        contact = request.form.get("contact")
        f_name = request.form.get("f_name")
        contact_2 = request.form.get("contact_2")
        yes = request.form.get("yes")
        yes_2 = request.form.get("yes_2")
        yes_3 = request.form.get("yes_3")
        yes_4 = request.form.get("yes_4")
        yes_5 = request.form.get("yes_5")
        yes_6 = request.form.get("yes_6")
        text_1 = request.form.get("text_1")
        text_2 = request.form.get("text_2")
        current_milage = request.form.get("current_milage")
        average = request.form.get("average")
        order = request.form.get("order")
        wheel = request.form.get("wheel")
        last_service_date = request.form.get("last_service_date")
        km = request.form.get("km")
        intervals = request.form.get("intervals")
        next_service = request.form.get("next_service")
        vehicle_2 = request.form.get("vehicle_2")
        tools = request.form.get("tools")
        defaults = request.form.get("defaults")
        current_driver = request.form.get("current_driver")
        signature_current_driver_date = request.form.get("current_sign_date")
        current_sign_time = request.form.get("current_sign_time")
        new_driver = request.form.get("new_driver")
        signature_new_driver_date = request.form.get("date_2")
        time_2 = request.form.get("time_2")
        person = request.form.get("person")
        signature_inspaction_person_date = request.form.get("date_3")
        time_3 = request.form.get("time_3")
        
        inspection = fleet_inspection_card_form(
            # date_1 = date_1,
            date_1 = convert_str_to_datetime_obj(date_1),
            time_1 = time_1,
            registration_1 = registration_1,
            fleet = fleet,
            milage_1 = milage_1,
            name = name,
            contact = contact,
            f_name = f_name,
            contact_2 = contact_2,
            yes = yes,
            yes_2 = yes_2,
            yes_3 = yes_3,
            yes_4 = yes_4,
            yes_5 = yes_5,
            yes_6 = yes_6,
            text_1 = text_1,
            text_2 = text_2,
            current_milage = current_milage,
            average = average,
            order = order,
            wheel = wheel,
            # last_service_date = last_service_date,
            last_service_date = convert_str_to_datetime_obj(last_service_date),
            km = km,
            intervals = intervals,
            next_service = next_service,
            vehicle_2 = vehicle_2,
            tools = tools,
            defaults = defaults,
            current_driver = current_driver,
            # signature_current_driver_date = signature_current_driver_date,
            signature_current_driver_date = convert_str_to_datetime_obj(signature_current_driver_date),
            current_sign_time = current_sign_time,
            new_driver = new_driver,
            # sinature_inspection_person_date = sinature_inspection_person_date,
            signature_new_driver_date = convert_str_to_datetime_obj(signature_new_driver_date),
            time_2 = time_2,
            person = person,
            # sinature_inspection_person_date = sinature_inspection_person_date,
            signature_inspaction_person_date = convert_str_to_datetime_obj(signature_inspaction_person_date),
            time_3 = time_3, 
        )

        db.session.add(inspection)
        db.session.commit()

    return render_template('driver_forms/fleet_inspection_card_form.html',
                reporting_card_class="router-link-active")