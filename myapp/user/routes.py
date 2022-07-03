from flask import (Blueprint, request, render_template, redirect,
                    url_for, flash)
import flask
from myapp.models import User
from myapp import db
from flask_login import (login_user, logout_user, 
                            login_required, current_user)


user = Blueprint("user", __name__)


@user.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.dashboard'))

    if request.method == "POST":
        email = request.form.get("email")
        password =  request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user.password == password:
            login_user(user)
            return redirect(url_for('user.dashboard'))
        else:
            flask("Incorrect Password!", "warning")
            return redirect(url_for("user.login"))

    return render_template("login.html")


@user.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        rpassword = request.form.get("rpassword")


        if password!=rpassword:
            flash("passwords are not matching.", "danger")
            return render_template("register.html")
        else:
            # Register the user
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash("You have been registered!", "success")
            return redirect(url_for('user.login'))
               
    return render_template("register.html")


@user.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@user.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("user.login"))