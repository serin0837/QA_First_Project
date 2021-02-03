from application import db


class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)


class Run(db.Model):
    run_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    km = db.Column(db.Float, nullable=False)
