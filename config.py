import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY", "you-will-never-guess!!!")
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    TEST = os.environ.get("TEST")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(basedir, "app.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ["microblog.service@outlook.com"]
    POSTS_PER_PAGE = 3
