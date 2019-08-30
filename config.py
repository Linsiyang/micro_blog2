import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))#获取当前.py文件的绝对路径

load_dotenv(os.path.join(basedir, 'microblog.env'))
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['your-email@example.com']
    POSTS_PER_PAGE = 25
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # 客户端授权密码

    LANGUAGES = ['en', 'zh']  # 注意：不要填写zh_CN。

    APPID = os.environ.get('APPID')
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')