from flask import render_template, request, redirect, url_for, flash
from . import auth
from app.auth.forms import LoginForm, RegisterForm
from models import Area, Role, User, Theme, Task
from app import db
from flask_login import login_user, logout_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    message = ""
    if request.method == 'POST':
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if login_form.validate_password_hash(user.password_hash):
                login_user(user)
                message = ('Bienvenido '+str(user.user_name))
                flash(message)
                return redirect(url_for('main.home'))
            else:
                message = ('Contraseña incorrecta')
        else:
            message = ('Correo inválido')
        
        if message != "":
            flash(message)

    context = {
        'login_form': login_form,
    }
    return render_template('auth/login.html', **context)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()

    choices = [('', '--Seleccione un área--'),]
    for choice in Area.query.all():
        choices.append((choice.id, str(choice.name)))
    
    register_form.area.choices = choices

    if request.method == 'POST':
        email = register_form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            flash(('Usuario existente, inicie sesión o use otro correo electrónico'))
            return redirect(url_for('auth.register'))
        
        password_hash = register_form.set_password_hash()
        area_id = Area.query.filter_by(id=register_form.area.data).first().id
        user = User(
            user_name=register_form.user_name.data, 
            email=email, 
            password_hash=password_hash, 
            area_id=area_id,
            role_id=2
        )
        message = user.add(user)
        flash(message)
        return redirect(url_for('auth.login'))

    context = {
        'register_form': register_form,
    }
    return render_template('auth/register.html', **context)

@auth.route('/logout')
def logout():
    logout_user()
    message = ('Vuelva pronto')
    flash(message)
    return redirect(url_for('auth.login'))