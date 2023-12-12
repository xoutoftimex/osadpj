from wtforms import Form, StringField, validators, DateField, PasswordField, EmailField


class CreateUserForm(Form):
    first_name = StringField('First Name', [
        validators.Length(min=1, max=50),
        validators.DataRequired()
    ])

    last_name = StringField('Last Name', [
        validators.Length(min=1, max=50),
        validators.DataRequired()
    ])

    username = StringField('Username', [
        validators.Length(min=1, max=50),
        validators.DataRequired()
    ])

    email = EmailField('Email', [
        validators.DataRequired(),
        validators.Email(),
        validators.Length(max=100)  # You can specify a max length for email
    ])

    date_of_birth = DateField('Date of Birth', [
        validators.DataRequired(message='Date of birth is required')
    ])

    password = PasswordField('Password', validators=[
        validators.DataRequired(),
        validators.Length(min=8, message='Password must be at least 8 characters long'),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])

    confirm_password = PasswordField('Confirm Password', validators=[
        validators.DataRequired()
    ])


class LoginForm(Form):

    email = StringField('Email', [
        validators.DataRequired(),
        validators.Email(),
        validators.Length(max=100)  # You can specify a max length for email
    ])

    password = PasswordField('Password', validators=[
        validators.DataRequired(),
        validators.Length(min=8, message='Password must be at least 8 characters long'),
    ])
