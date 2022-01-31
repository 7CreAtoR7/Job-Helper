import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask_login import UserMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


# создание таблицы соискателей
class Users(SqlAlchemyBase, UserMixin):
    __tablename__ = 'job-seekers'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)
    is_worker = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    resumes = orm.relation("Resumes", back_populates='resum')

    # связь с таблицей employers

    def __repr__(self):
        return f'<User> {self.id} {self.surname} {self.name}'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
