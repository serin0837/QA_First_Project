from application import db
# from flask import Flask, render_template, request
# from flask_wtf import FlaskForm


class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)
    # id = db.Column(db.Integer)
    # password = db.Column(db.Integer)


class Run(db.Model):
    run_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    km = db.Column(db.Float, nullable=False)
