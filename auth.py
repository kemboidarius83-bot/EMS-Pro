from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint("auth", __name__)

USERNAME = "admin"
PASSWORD = "admin123"

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("dashboard"))

        return "Invalid username or password"

    return render_template("login.html")
