from random import choice
from forms.user import MainSeeker, LoginSeeker, RegisterSeeker, CreateResume, MainEmployer, \
    RegisterEmployer, LoginEmployer, CreateVacancy
from data.resumes import Resumes
from data.users import Users
from data.employers import Employers

from data.vacancies import Vacancies
from flask import render_template, request, redirect, Flask, flash
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

# задний фон на первую страницу
photos = ['/static/img/bg1.jpg', '/static/img/bg2.jpg', '/static/img/bg3.jpg', '/static/img/bg4.jpg']


def main():
    db_session.global_init(f"db/all_Users.db")
    db_sess = db_session.create_session()
    app.run(debug=True)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Users).get(user_id)


# обработчик стартовой страницы с выбором работодателя/соискателя
@app.route('/')
def start_page():
    return render_template('base.html', picture=choice(photos))


# /employer
@app.route('/employer', methods=['GET', 'POST'])
def employer_page():
    db_session.global_init(f"db/all_Users.db")
    db_sess = db_session.create_session()

    resumes = db_sess.query(Resumes).all()
    form = MainEmployer()
    if form.validate_on_submit():
        if form.resumes_line.data == '':
            important_resumes = db_sess.query(Resumes).all()
            return render_template('employer.html', form=form, jobs=important_resumes)
        else:
            key_words = form.resumes_line.data.lower().split(' ')
            if len(key_words) == 1:
                important_resumes = db_sess.query(Resumes).filter(Resumes.desired_position.like(f"%{key_words[0]}%"))
                return render_template('employer.html', form=form, jobs=important_resumes)

    return render_template('employer.html', form=form, jobs=resumes)


# /work-seeker
@app.route('/work-seeker', methods=['GET', 'POST'])
def work_seeker_page():
    db_session.global_init(f"db/all_Users.db")
    db_sess = db_session.create_session()

    vacancies = db_sess.query(Vacancies).all()

    form = MainSeeker()
    if form.validate_on_submit():
        if form.vacancy.data == '':
            important_vacancies = db_sess.query(Vacancies).all()
            return render_template('seeker.html', form=form, jobs=important_vacancies)
        else:
            key_words = form.vacancy.data.lower().split()
            if len(key_words) == 1:
                important_vacancies = db_sess.query(Vacancies).filter(Vacancies.vacancy_name.like(f"%{key_words[0]}%"))
                return render_template('seeker.html', form=form, jobs=important_vacancies)

    return render_template('seeker.html', form=form, jobs=vacancies)


@app.route('/login/seeker', methods=['GET', 'POST'])
def login_seeker():
    form = LoginSeeker()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Users).filter(Users.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/work-seeker")
        return render_template('seeker_login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('seeker_login.html', title='Авторизация', form=form)


@app.route('/login/employer', methods=['GET', 'POST'])
def login_employer():
    form = LoginEmployer()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Employers).filter(Employers.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/employer")
        return render_template('employer_login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('employer_login.html', title='Авторизация', form=form)


@app.route('/create_resume', methods=['GET', 'POST'])
def seeker_create_resume():
    form = CreateResume()
    if request.method == 'POST':
        flash('Резюме успешно размещено!')
        db_session.global_init(f"db/all_Users.db")
        db_sess = db_session.create_session()

        current_seeker = db_sess.query(Users).filter(Users.email == form.email.data).first()

        # Добавляем в таблицу с резюменовое резюме
        new_resume = Resumes(
            creator_id=current_seeker.id,
            name=form.name.data,
            surname=form.surname.data,
            birthday=form.birthday.data,
            sex=form.sex.data,
            phone=form.phone.data,
            ready_to_move=form.ready_to_move.data,
            level_edu=form.level_edu.data,
            college=form.faculty.data,
            speciality=form.specialty.data,
            finish_year=form.finish_year.data,
            is_language_eng=form.knows_english.data,
            job_exp=form.work_exp.data,
            desired_position=form.desired_position.data,
            salary=form.salary.data,
            employment=form.employment.data,
            work_hours=form.work_hours.data,
            organisation=form.organisation.data,
            region=form.region.data,
            website_of_organisation=form.website_of_ur_organisation.data,
            field_of_activity=form.field_of_activity_the_company.data,
            post=form.post.data,
            job_start=form.start_work_year.data,
            job_finish=form.finish_work_year.data,
            achievements=form.achievements.data,
            skills=form.skills.data
        )
        db_sess.add(new_resume)
        db_sess.commit()

    return render_template('create_resume.html', form=form)


@app.route('/create_vacancy', methods=['GET', 'POST'])
def employer_create_vacancy():
    form = CreateVacancy()
    if request.method == 'POST':
        flash('Вакансия успешно размещена!')
        db_session.global_init(f"db/all_Users.db")
        db_sess = db_session.create_session()

        current_employer = db_sess.query(Employers).filter(Employers.email == form.email.data).first()

        new_vacancy = Vacancies(
            creator_id=current_employer.id,
            vacancy_name=form.name.data,
            city=form.city.data,
            specialty=form.speciality.data,
            office_address=form.office_address.data,
            salary=form.salary.data,
            description=form.description.data,
            skills=form.key_skills.data,
            work_experience=form.work_exp.data,
            work_hours=form.work_hrs.data,
            employment=form.employment.data,
            phone=form.phone.data
        )
        db_sess.add(new_vacancy)
        db_sess.commit()

    return render_template('create_vacancy.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register/seeker', methods=['GET', 'POST'])
def register_seeker():
    form = RegisterSeeker()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('seeker_register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(Users).filter(Users.email == form.email.data).first():
            return render_template('seeker_register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = Users(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            is_worker=1
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login/seeker')
    return render_template('seeker_register.html', title='Регистрация', form=form)


@app.route('/register/employer', methods=['GET', 'POST'])
def register_employer():
    form = RegisterEmployer()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('employer_register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(Users).filter(Users.email == form.email.data).first():
            return render_template('employer_register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        new_employer = Employers(
            name=form.name.data,
            surname=form.surname.data,
            phone=form.phone.data,
            email=form.email.data,
            company=form.company_name.data,
            region=form.region.data,
            is_employer=1
        )
        new_employer.set_password(form.password.data)
        db_sess.add(new_employer)
        db_sess.commit()
        return redirect('/login/employer')
    return render_template('employer_register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
