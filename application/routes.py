from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Register


@app.route('/', methods=["GET", "POST"])
def home():
    if request.form:
        person = Register(name=request.form.get("name"))
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees)


@app.route("/update", methods=["POST"])
def update():
    person = Register.query.filter_by(name=request.form.get("oldname")).first()
    person.name = request.form.get("newname")
    db.session.commit()
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    person = Register.query.filter_by(name=request.form.get("name")).first()
    db.session.delete(person)
    db.session.commit()
    return redirect("/")


# Adding Run
# @app.route("/addRun", methods=['GET', 'POST'])
# def addRun():
#     form = AddRun()
#     if form.validate_on_submit():
#         run_to_add = Product(
#             km=form.km.data)
#         db.session.add(run_to_add)
#         db.session.commit()
#         return redirect(url_for('addRun'))
