from application import app
from flask import Flask, render_template, request, redirect

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
