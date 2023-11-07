import os

class Config:
    SECRET_KEY = '6d73cfc6e3f69e33029f6c9f0b218105'
    SQLALCHEMY_DATABASE_URI ="sqlite:///site.db"
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT =587
    MAIL_USE_TLS =True
    MAIL_USERNAME =os.environ.get('EMAIL_USER')
    MAIL_PASSWORD =os.environ.get('EMAIL_PASS')
