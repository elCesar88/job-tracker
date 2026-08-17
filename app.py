from flask import Flask, render_template, request, redirect, url_for, abort
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


@app.route("/edit/<int:app_id>", methods=["GET", "POST"])
def edit(app_id):
    application = db.get_application(app_id)
    if application is None:
        abort(404)

    if request.method == "POST":
        db.update_application(
            app_id,
            company=request.form["company"],
            role=request.form["role"],
            status=request.form["status"],
            date_applied=request.form["date_applied"],
        )
        return redirect(url_for("home"))

    return render_template("edit.html", application=application)
