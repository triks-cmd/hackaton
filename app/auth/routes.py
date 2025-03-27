from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.auth.forms import RegistrationForm, LoginForm
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid email or password', 'danger')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))