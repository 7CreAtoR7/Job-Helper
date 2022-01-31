from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, DateField, TextAreaField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class MainSeeker(FlaskForm):
    vacancy = StringField('')
    submit = SubmitField('Найти')


class MainEmployer(FlaskForm):
    resumes_line = StringField('')
    submit = SubmitField('Найти')


class LoginSeeker(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class LoginEmployer(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterSeeker(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class RegisterEmployer(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    phone = StringField('Телефон 8-xxx-xxx-xx-xx', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    company_name = StringField('Название компании', validators=[DataRequired()])
    region = StringField('Регион', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class CreateResume(FlaskForm):
    name = StringField('Имя*', validators=[DataRequired()])
    surname = StringField('Фамилия*', validators=[DataRequired()])
    birthday = DateField('Дата рождения*', validators=[DataRequired()])
    sex = StringField('Пол*', validators=[DataRequired()])
    phone = StringField('Телефон* (8-xxx-xxx-xx-xx)', validators=[DataRequired()])
    email = EmailField('Почта*', validators=[DataRequired()])
    ready_to_move = BooleanField('Готов к переезду')
    level_edu = StringField('Образование')
    faculty = StringField('Институт')
    specialty = StringField('Специальность')
    finish_year = DateField('Год окончания')
    his_language = StringField('Родной язык*', validators=[DataRequired()])
    knows_english = BooleanField('Английский язык')
    work_exp = StringField('Опыт работы (в годах)*', validators=[DataRequired()])
    desired_position = StringField('Желаемая должность')
    salary = StringField('Желаемая зарплата')
    employment = StringField('Занятость*', validators=[DataRequired()])
    work_hours = StringField('График работы*', validators=[DataRequired()])
    organisation = StringField('Организация')
    region = StringField('Регион')
    website_of_ur_organisation = StringField('Сайт организации')
    field_of_activity_the_company = StringField('Сфера деятельности компании')
    post = StringField('Занимаемая должность')
    start_work_year = DateField('Начало работы')
    finish_work_year = DateField('Окончание')
    achievements = TextAreaField('Обязанности, функции, достижения*', validators=[DataRequired()])
    skills = TextAreaField('Навыки*', validators=[DataRequired()])
    submit = SubmitField('Разместить резюме')


class CreateVacancy(FlaskForm):
    name = StringField('Название вакансии*', validators=[DataRequired()])
    city = StringField('Вакансия в городе*', validators=[DataRequired()])
    speciality = StringField('Специализации*', validators=[DataRequired()])
    phone = StringField('Телефон* (8-xxx-xxx-xx-xx)', validators=[DataRequired()])
    office_address = StringField('Адрес офиса')
    email = EmailField('Почта*', validators=[DataRequired()])
    salary = StringField('Предполагаемый уровень дохода (1000-2000) р')
    description = TextAreaField('Описание*', validators=[DataRequired()])
    key_skills = TextAreaField('Ключевые навыки')
    work_exp = StringField('Опыт работы* (в годах)', validators=[DataRequired()])
    work_hrs = StringField('График работы')
    employment = StringField('Тип занятости')

    submit = SubmitField('Разместить вакансию')
