from flask import render_template
from . import main
from flask_login import login_required, current_user

@main.route('/home')
@login_required
def home():
    print(current_user)

    return render_template('main/home.html')