from myproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


########
@app.route('/')
def home():
    return render_template('home.html')

#########

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')