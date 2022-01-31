import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


# создание таблицы вакансий и настрйока связи с таблицей employers
class Vacancies(SqlAlchemyBase):
    __tablename__ = 'vacancies'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    creator_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("employers.id"))
    vacancy_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    specialty = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    office_address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    salary = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    skills = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_experience = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_hours = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    employment = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'<Vacancy> {self.id} {self.creator_id} {self.vacancy_name} {self.city} {self.specialty} {self.office_address} {self.salary} {self.description} {self.skills} {self.work_experience} {self.work_hours} {self.employment} {self.phone}'

    employer = orm.relation('Employers')
