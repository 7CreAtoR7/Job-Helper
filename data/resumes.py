import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


# создание таблицы резюме и настрйока связи с таблицей job-seekers
class Resumes(SqlAlchemyBase):
    __tablename__ = 'resumes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    creator_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("job-seekers.id"))
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    birthday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sex = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ready_to_move = sqlalchemy.Column(sqlalchemy.Boolean, default=False)  # готов к переезду
    level_edu = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    college = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # институт
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # специальность
    finish_year = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    is_language_eng = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    job_exp = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    desired_position = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # желаемая должность
    salary = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # желаемая зп
    employment = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # тип занятости
    work_hours = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # график работы
    organisation = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # компания (если где-то работали)
    region = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    website_of_organisation = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    field_of_activity = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # сфера деятельности компании
    post = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # твоя должность
    job_start = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    job_finish = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    achievements = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    skills = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    resum = orm.relation('Users')
