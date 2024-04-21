"""Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class Register(FlaskForm):
    user_name = StringField('User_name', validators=[DataRequired()])
    user_surname = StringField('User_surname', validators=[DataRequired()])
    user_email = StringField('User_email', validators=[DataRequired(), Email()])
    # user_email = EmailField('User_email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm_Password', validators=[DataRequired(), EqualTo('password')])
