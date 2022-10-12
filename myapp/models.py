
from email.policy import default
from myapp import db
from datetime import datetime
from myapp import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(70))
    joining_date = db.Column(db.DateTime, default=datetime.now)
    password = db.Column(db.String(400))
    
    is_admin = db.Column(db.Boolean, default=False)
    
    # Extra field for drivers
    employee_no = db.Column(db.Integer, unique=False, nullable=True)
    # change registration_no to "employee_no"
    fleet_no = db.Column(db.Integer, unique=False, nullable=True)
    milage = db.Column(db.Integer, unique=False, nullable=True)
    driver_license_image = db.Column(db.String(200), unique=False, nullable=True)
    id_no_image = db.Column(db.String(200), unique=False, nullable=True)
    drivers_license_no = db.Column(db.Integer, unique=False, nullable=True)
    drivers_license_endorced = db.Column(db.String(5), unique=False, nullable=True)
    drivers_license_renewal_date = db.Column(db.Date, default=datetime.now().date)
    
    # driver contact details
    cell_no = db.Column(db.Integer, unique=False, nullable=True)
    family_members = db.Column(db.String(300), unique=False, nullable=True)
    # email address is defined above
    # password is defined above.
    
    # Adding relationship of one to one with vehicle
    vehicle = db.relationship("Vehicle", backref="driver", uselist=False)
    
    
    # Adding relationship of one to one with fleetcard
    fleet_card = db.relationship("FleetCard", backref="fleet_card_driver", uselist=False)
    
    # Adding relationship of one to one with vehicle
    maintanance = db.relationship("MaintenancesTyres", backref="driver_maintanance", lazy='dynamic')
    
    # Adding relationship of one to one with vehicle expense
    vehicle_expense = db.relationship("VehicleExpense", backref="vehicle_expense", uselist=True)
    
    def __repr__(self):
        return f"{self.username} - assigned_vehicle: {self.vehicle}"


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registration_no = db.Column(db.Integer, nullable=False, unique=False)
    financer = db.Column(db.String(100), nullable=False, unique=False)
    account_no = db.Column(db.Integer, nullable=False, unique=False)
    original_capital_balance = db.Column(db.Integer, nullable=False, unique=False)
    installment_amount = db.Column(db.Integer, nullable=False, unique=False)
    frequency_of_installment = db.Column(db.Integer, nullable=False, unique=False)
    date_commenced = db.Column(db.Date, nullable=False, unique=False, default=datetime.now().date)
    expiry_date = db.Column(db.Date, nullable=False, unique=False, default=datetime.now().date)
    original_term = db.Column(db.Integer, nullable=False, unique=False)
    
    remaining_installments = db.Column(db.Integer, nullable=False, unique=False)
    balloon_risidual = db.Column(db.String(100), nullable=False, unique=False)
    outstanding_capital_balance = db.Column(db.Integer, nullable=False, unique=False)
    advance_amount = db.Column(db.Integer, nullable=False, unique=False)
    actual_contract_balance = db.Column(db.Integer, nullable=False, unique=False)
    interest_rate = db.Column(db.Integer, nullable=False, unique=False)
    take_on_odo = db.Column(db.String(100), nullable=False, unique=False)
    
    vehicle_manufacturer = db.Column(db.String(100), nullable=False, unique=False)
    date_of_first_registration = db.Column(db.Date, default=datetime.now().date)
    model = db.Column(db.String(25), nullable=False, unique=False)
    color = db.Column(db.String(25), nullable=False, unique=False)
    mobile_number = db.Column(db.Integer, nullable=True, unique=False)
    engine_no = db.Column(db.String(50), nullable=False, unique=False)
    vin_no = db.Column(db.String(50), nullable=False, unique=False)
    tank_capacity = db.Column(db.String(50), nullable=False, unique=False)
    license_disk_expiry_date = db.Column(db.Date, default=datetime.now().date)
    license_disk_renewal_date = db.Column(db.Date, default=datetime.now().date)
    
    # Adding relationship back to driver
    driver_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True, nullable=True)
    
    # Adding relationship of one to one with vehicle expense table
    vehicle = db.relationship("VehicleExpense", backref="vehicle", uselist=False)
    
    def __repr__(self):
        return f"{self.registration_no}, financer: {self.financer}"


class VehicleExpense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fuel_value = db.Column(db.Integer)
    oil_value = db.Column(db.Integer)
    repair_and_maint = db.Column(db.Integer)
    tyre_value = db.Column(db.Integer)
    accident_value = db.Column(db.Integer)
    other_value = db.Column(db.Integer)
    toll_value = db.Column(db.Integer)
    
    # Adding relationship back to Vehicle
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), unique=False, nullable=True)
    
    # Adding relationship back to Vehicle
    driver_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False, nullable=True)
    
    def __repr__(self):
        return f"{self.id}"


# Fleet card order form table for storing
# data of drivers request
class FleetCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registration_no = db.Column(db.String(50))
    driver = db.Column(db.String(60))
    take_on_odo = db.Column(db.String(100))
    vehicle_manufacturer = db.Column(db.String(100))
    date_of_first_registration = db.Column(db.Date, default=datetime.now().date)
    model = db.Column(db.String(50))
    color = db.Column(db.String(50))
    mobile_number = db.Column(db.String(20))
    engine_no = db.Column(db.String(50))
    vin_no = db.Column(db.String(50))
    tank_capacity = db.Column(db.String(50))
    employee_no = db.Column(db.String(50))
    
    # Adding relationship back to driver
    driver_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True, nullable=True)


class MaintenancesTyres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    reg_num = db.Column(db.String(50))
    yr_mth = db.Column(db.DateTime, default=datetime.now())
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    fuel_value = db.Column(db.String(50))
    km_travelled = db.Column(db.String(50))
    oil_value = db.Column(db.String(50))
    km = db.Column(db.String(50))
    repair_and_maint = db.Column(db.String(50))
    maintenance_plan = db.Column(db.String(50))

    maintenance_expiry_year_month_km_date = db.Column(db.DateTime, default=datetime.now)

    type_of_service = db.Column(db.String(50))
    service_intervals = db.Column(db.String(50))
    tyre_value = db.Column(db.String(50))
    accident_value = db.Column(db.String(50))
    accident_incident = db.Column(db.String(50))
    other_value = db.Column(db.String(50))
    description = db.Column(db.String(50))
    toll_value =   db.Column(db.String(50))


class FleetIncidentReporting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.String(50))
    id_number_1 = db.Column(db.Integer)
    license_no_1 = db.Column(db.Integer)
    driver_licencse_date_issued_1 = db.Column(db.DateTime, default=datetime.now)
    code_1 = db.Column(db.String(50))
    endorsed_1 = db.Column(db.String(50))
    do_you_have_your_own_insurance = db.Column(db.String(50))
    details_of_your_insurance = db.Column(db.String(100))
    details_of_previous_accidents = db.Column(db.String(100))
    registration_no_1 = db.Column(db.Integer)
    milage = db.Column(db.Integer)
    make_1 = db.Column(db.String(50))
    model_1 = db.Column(db.String(50))
    reason_for_passenger_in_vehicle = db.Column(db.String(50))
    is_the_passenger_a_employee = db.Column(db.String(50))
    name_surname_of_passenger = db.Column(db.String(50))
    id_no_attach_copy_of_id = db.Column(db.Integer)
    address_1 = db.Column(db.String(100))
    details_of_injury_is = db.Column(db.String(100))
    names_and_surname_of_driver = db.Column(db.String(50))
    contact_details = db.Column(db.String(100))
    id_number_2 = db.Column(db.Integer)
    license_no_2 = db.Column(db.Integer)
    driver_license_date_issued_2 = db.Column(db.DateTime, default=datetime.now)
    code = db.Column(db.String(50))
    endorsed = db.Column(db.String(50))
    address_2 = db.Column(db.String(100))
    company_name = db.Column(db.String(50))
    company_address = db.Column(db.String(100))
    contact_person = db.Column(db.String(100))
    telephone_no = db.Column(db.Integer)
    email_address = db.Column(db.String(50))
    registration_no_2 = db.Column(db.Integer)
    colour_1 = db.Column(db.String(50))
    make_2 = db.Column(db.String(50))
    model_2 = db.Column(db.String(50))
    registration_no_3 = db.Column(db.Integer)
    colour_2 = db.Column(db.String(50))
    make_3 = db.Column(db.String(50))
    model_3 = db.Column(db.String(50))
    details_of = db.Column(db.String(100))
    saps_case_no = db.Column(db.Integer)
    take_photo_1 = db.Column(db.String(50))
    take_photo_2 = db.Column(db.String(50))
    manager_1 = db.Column(db.String(50))
    reporting_date_1 = db.Column(db.DateTime, default = datetime.now)
    time_1 = db.Column(db.String(50))
    manager_2 = db.Column(db.String(50))
    reporting_date_2 = db.Column(db.DateTime, default = datetime.now)
    time_2 = db.Column(db.String(50))

class FleetNcIncidentReporting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registration_no = db.Column(db.Integer)
    vin = db.Column(db.Integer)
    make = db.Column(db.String(50))
    vehicle_manufacturer = db.Column(db.String(50))
    License = db.Column(db.Integer)

    driver_licence_date_issued = db.Column(db.DateTime, default = datetime.now)

    code = db.Column(db.Integer)
    endorsed = db.Column(db.String(50))
    License_2 = db.Column(db.Integer)

    driver_licence_date_issued_2 = db.Column(db.DateTime, default = datetime.now)

    Code_2 = db.Column(db.Integer)
    endorsed_2 = db.Column(db.String(50))
    demage = db.Column(db.String(50))
    demage_2 = db.Column(db.String(50))
    yes_no = db.Column(db.String(50))
    manager = db.Column(db.String(50))

    reporting_date = db.Column(db.DateTime, default = datetime.now)

    time = db.Column(db.String(50))
    yes_no_2 =  db.Column(db.String(50))
    manager_2 = db.Column(db.String(50))

    reporting_date_2 = db.Column(db.DateTime, default = datetime.now)

    time_2 = db.Column(db.String(50))


class fleet_inspection_card_form(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_1 = db.Column(db.DateTime, default = datetime.now)
    time_1 = db.Column(db.String(50))
    registration_1 = db.Column(db.Integer)
    fleet = db.Column(db.Integer)
    milage_1 = db.Column(db.Integer)
    name = db.Column(db.String(50))
    contact = db.Column(db.String(100))
    f_name = db.Column(db.String(50))
    contact_2 = db.Column(db.String(100))
    yes = db.Column(db.String(50))
    yes_2 = db.Column(db.String(50))
    yes_3 = db.Column(db.String(50))
    yes_4 = db.Column(db.String(50))
    yes_5 = db.Column(db.String(50))
    yes_6 = db.Column(db.String(50))
    text_1 = db.Column(db.String(100))
    text_2 = db.Column(db.String(100))
    current_milage = db.Column(db.String(50))
    average = db.Column(db.String(50))
    order = db.Column(db.String(50))
    wheel = db.Column(db.String(50))
    last_service_date = db.Column(db.DateTime, default = datetime.now)
    km = db.Column(db.String(50))
    intervals = db.Column(db.String(50))
    next_service = db.Column(db.String(50))
    vehicle_2 = db.Column(db.String(100))
    tools = db.Column(db.String(100))
    defaults = db.Column(db.String(100))
    current_driver = db.Column(db.String(50))
    signature_current_driver_date = db.Column(db.DateTime, default = datetime.now)
    current_sign_time = db.Column(db.String(50))
    new_driver = db.Column(db.String(50))
    signature_new_driver_date = db.Column(db.DateTime, default = datetime.now)
    time_2 = db.Column(db.String(50))
    person = db.Column(db.String(100))
    signature_inspaction_person_date = db.Column(db.DateTime, default = datetime.now)
    time_3 = db.Column(db.String(50))