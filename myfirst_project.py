from flask import Flask, render_template, request, redirect, url_for
import sqlalchemy
from database import User, app, db

@app.route('/', methods=['GET', 'POST'])
def Main():
    users = User.AllUsers()
    
    if request.method == 'POST':
        user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=request.form['password']
        )
        user.AddUser(user)
        
        return redirect(url_for('Main'))
    
    return render_template('plantilla1.html', users=users)

if __name__ == '_main__':
    app.run(debug=True, port=5000)