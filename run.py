# -*- coding: utf-8 -*-

# @Date    : 2018-11-28
# @Author  : Peng Shiyu


import os
import sys

from flask import Flask

from api_app.controller import api_app

from html_app.controller import html_app
from scheduler_app.controller import scheduler_app
from version import VERSION
from flask_basicauth import BasicAuth

# 把当前目录加入执行路径，不然找不到用户自定义config.py文件
sys.path.insert(0, os.getcwd())

try:
    import config
except Exception as e:
    import default_config as config

app = Flask(__name__)

app.secret_key = config.SECRET_KEY

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['BASIC_AUTH_USERNAME'] = config.BASIC_AUTH_USERNAME
app.config['BASIC_AUTH_PASSWORD'] = config.BASIC_AUTH_PASSWORD

app.config['BASIC_AUTH_FORCE'] = config.BASIC_AUTH_FORCE

basic_auth = BasicAuth(app)

app.register_blueprint(blueprint=html_app, url_prefix="/")
app.register_blueprint(blueprint=api_app, url_prefix="/api")
app.register_blueprint(blueprint=scheduler_app, url_prefix="/scheduler")


def main():
    # 初始化解析器
    if len(sys.argv) == 2:
        init = sys.argv[1]

        # 初始化项目
        if init == "init":
            import shutil
            import os
            base_dir = os.path.dirname(os.path.abspath(__file__))
            default_config = os.path.join(base_dir, "default_config.py")
            shutil.copy(default_config, "./config.py")
            print("spideradmin init successful!")

        # 查看版本号
        elif init == '-v':
            print("spideradmin version:", VERSION)
        else:
            print("you may need: spideradmin init ?")
    else:
        app.run(config.HOST, config.PORT)


if __name__ == '__main__':
    app.run(debug=True)
