from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, ValidationError, DataRequired
from app.models import loginn


class RegistrationForm(FlaskForm):
    nama = StringField('Nama',validators=[InputRequired(), Length(max=100)], render_kw={"placeholder": "Nama"})
    username = StringField('Username',validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    email = StringField('Email',validators=[InputRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[InputRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = loginn.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = loginn.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()], render_kw={"placeholder": "Username"})
    # email = StringField('Email',validators=[InputRequired(), Email()])
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

# class UpdateAccountForm(FlaskForm):
#     username = StringField('Username',validators=[InputRequired(), Length(min=2, max=20)])
#     email = StringField('Email',validators=[InputRequired(), Email()])
#     picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
#     submit = SubmitField('Update')

#     def validate_username(self, username):
#         if username.data != current_user.username:
#             user = User.query.filter_by(username=username.data).first()
#             if user:
#                 raise ValidationError('That username is taken. Please choose a different one.')

#     def validate_email(self, email):
#         if email.data != current_user.email:
#             user = User.query.filter_by(email=email.data).first()
#             if user:
#                 raise ValidationError('That email is taken. Please choose a different one.')

# class PostForm(FlaskForm):
#     picture = FileField('Choose a car image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
#     submit = SubmitField('Detect Licence Plate')

#class MailForm(FlaskForm):
    