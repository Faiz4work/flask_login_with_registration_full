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
    registration_no = db.Column(db.Integer, unique=False, nullable=True)
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
    
    
    
    def __repr__(self):
        return f"{self.username}, {self.email}, is_admin: {self.is_admin}"


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
    
    def __repr__(self):
        return f"id: {self.id}, registration: {self.registration_no}, financer: {self.financer}"










