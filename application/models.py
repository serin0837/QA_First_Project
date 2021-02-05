from application import db


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    done = db.Column(db.String(100))
    date = db.Column(db.String(30))
    goal = db.relationship('Goal', backref='exercise')

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal_name = db.Column(db.String(30))
    goal_setdate = db.Column(db.String(30))
    goal_finishdate = db.Column(db.String(30))
    goal_success = db.Column(db.Boolean)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
