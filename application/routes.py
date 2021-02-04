from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Goal, Exercise

db.create_all()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.form:
        exercise = Exercise(name=request.form.get("name"),
                            done=request.form.get("done"),
                            date=request.form.get("date"))
        db.session.add(exercise)
        db.session.commit()
    exercises = Exercise.query.all()
    return render_template("home.html", exercises=exercises)


@app.route("/update", methods=["POST"])
def update():
    exercise = Exercise.query.filter_by(
        name=request.form.get("oldname")).first()
    exercise.name = request.form.get("newname")
    exercise.done = request.form.get("newdone")
    exercise.date = request.form.get("newdate")
    db.session.commit()
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    exercise = Exercise.query.filter_by(name=request.form.get("name")).first()
    db.session.delete(exercise)
    db.session.commit()
    return redirect("/")


# edit goal
@app.route("/goal", methods=['GET', 'POST'])
def editgoal():
    if request.form:
        goal = Goal(goal_name=request.form.get("goal_name"),
                    goal_setdate=request.form.get("goal_setdate"),
                    goal_finishdate=request.form.get("goal_finishdate"),
                    exercise_id=request.form.get("exercise_id")
                    )
        db.session.add(goal)
        db.session.commit()
    goals = Goal.query.all()
    return render_template("edit_goal.html", goals=goals)

@app.route("/update-goal", methods=["POST"])
def updategoal():
    goal = Goal.query.filter_by(
        id = request.form.get("oldid")).first()
    goal.goal_name = request.form.get("newname")
    goal.goal_setdate = request.form.get("newsetdate")
    goal.goal_finishdate = request.form.get("newfinishdate")
    db.session.commit()
    return redirect("/goal")

@app.route("/delete-goal", methods=["POST"])
def deletegoal():
    goal = Goal.query.filter_by(id=request.form.get("id")).first()
    db.session.delete(goal)
    db.session.commit()
    return redirect("/goal")