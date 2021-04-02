from flask import render_template, request
from . import auth
from app.auth.forms import LoginForm, RegisterForm
from models import Area

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == 'POST':
        print(login_form.email.data)

    context = {
        'login_form': login_form,
    }
    return render_template('auth/login.html', **context)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()

    choices = [('', '--Seleccione un área--'),]
    for choice in Area.query.all():
        choices.append((str(choice.name), str(choice.name)))
    
    register_form.area.choices = choices

    if request.method == 'POST':
        print(register_form.email.data)

    context = {
        'register_form': register_form,
    }
    return render_template('auth/register.html', **context)