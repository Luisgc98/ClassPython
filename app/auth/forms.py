from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, DateField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, DataRequired
from werkzeug.security import generate_password_hash, check_password_hash

class LoginForm(FlaskForm):
    email = StringField(label=('Nombre de usuario o correo electrónico'), validators=[DataRequired()])
    password = PasswordField(label=('Contraseña'), validators=[DataRequired()])
    submit = SubmitField(label='Ingresar')
    
    def validate_password_hash(self, password_hash):
        return check_password_hash(password_hash, self.password.data)

class RegisterForm(FlaskForm):
    email = EmailField(label=('Correo electrónico'), validators=[DataRequired()])
    user_name = StringField(label=('Nombre de usuario'), validators=[DataRequired()])
    password = PasswordField(label=('Contraseña'), validators=[DataRequired()])
    confirm_password = PasswordField(label=('Confirmar contraseña'), validators=[DataRequired()])
    area = SelectField(label=('Área'), validators=[DataRequired()])
    theme_code = StringField(label=('Código de Activación'))
    submit = SubmitField(label='Registrar')
    
    def set_password_hash(self):
        return generate_password_hash(self.password.data)