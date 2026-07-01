from flask import Blueprint, render_template

employee = Blueprint("employee", __name__)

@employee.route("/employees")
def employees():
    return render_template("employees.html")

@employee.route("/add-employee")
def add_employee():
    return render_template("add_employee.html")
