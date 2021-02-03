from application import db


class Exercise(db.Model):
    name = db.Column(db.String(30), nullable=False,  primary_key=True)
    done = db.Column(db.String(100))


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    goal_name = db.Column(db.String, nullable=False)
    goal_setdate = db.Column(db.String, nullable=False)
    goal_finishdate = db.Column(db.String, nullable=False)
    goal_success = db.Column(db.Boolean, nullable=False)
