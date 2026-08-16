from flask import Flask, render_template, request, redirect, url_for
import db


app = Flask(__name__)
db.init_db()


@app.route("/")
def home():
    applications = db.get_all_applications()
    return render_template("home.html", applications=applications)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        db.add_application(
            company=request.form["company"],
            role=request.form["role"],
            status=request.form["status"],
            date_applied=request.form["date_applied"],
        )
        return redirect(url_for("home"))
    return render_template("add.html")
