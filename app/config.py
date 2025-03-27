import os

class Config:
    SECRET_KEY = 'ваш_секретный_ключ_123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False