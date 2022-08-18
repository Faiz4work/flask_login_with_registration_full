from flask import (Blueprint, render_template, redirect, url_for, flash)
from myapp.models import Vehicle
from flask_login import current_user, login_required

expense_and_reports = Blueprint("expense_and_reports", __name__)

@expense_and_reports.route("/vehicle_expense")
@login_required
def vehicle_expense():
    vehicle = Vehicle.query.filter_by(driver_id=current_user.id).first()
    return render_template("expenses/vehicle_expense_form.html",
                           vehicle=vehicle)
    

@expense_and_reports.route("/fleet_card_form")
@login_required
def fleet_card_form():
    return render_template("expenses/fleet_card_form.html")