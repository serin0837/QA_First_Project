from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Goal, Exercise
from application.forms import GoalForm

db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.form:
        exercise = Exercise(name=request.form.get("name"),
                            done=request.form.get("done"))
        db.session.add(exercise)
        db.session.commit()
    exercises = Exercise.query.all()
    return render_template("edit_exercise.html", exercises=exercises)


@app.route("/update", methods=["POST"])
def update():
    exercise = Exercise.query.filter_by(
        name=request.form.get("oldname")).first()
    exercise.name = request.form.get("newname")
    exercise = Exercise.query.filter_by(
        name=request.form.get("oldone")).first()
    exercise.done = request.form.get("newdone")
    db.session.commit()
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    exercise = Exercise.query.filter_by(name=request.form.get("name")).first()
    db.session.delete(exercise)
    db.session.commit()
    return redirect("/")


# edit goal
@app.route("/edit_goal", methods=['GET', 'POST'])
def editgoal():
    form = GoalForm()
    if form.validate_on_submit():
        goal_to_add = Goal(
            goal_name=form.goal_name.data,
            goal_setdate=form.goal_setdate.data,
            goal_finishdate=form.goal_finishdate.data,
            goal_success=form.goal_success.data
        )
        db.session.add(goal_to_add)
        db.session.commit()
        return redirect(url_for('edit_goal'))
