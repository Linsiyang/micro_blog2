#从flask包中导入Flask类
from flask import Flask
from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from config import Config#从config模块导入Config类
import logging
from logging.handlers import RotatingFileHandler
import os


#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app = Flask(__name__)
app.config.from_object(Config)
moment = Moment(app)


login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app)
bootstrap = Bootstrap(app)


db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象



if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes,models,errors #永远最后
#导入一个新模块models，它将定义数据库的结构，目前为止尚未编写