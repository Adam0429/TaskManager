from task import Task
import os
import os
from glob import glob
from flask import Flask, render_template,request,redirect,Response,jsonify,make_response
import datetime
from consumer.emailconsumer import EmailConsumer
from configparser import ConfigParser
from consumer.logconsumer import LogConsumer
from flask_cors import CORS 
from utils.simple_utils import str_dict

app = Flask(__name__)
app.config['task_path'] = 'task_code'
app.config['JSON_AS_ASCII'] = False
CORS(app) # 解决跨域问题

class Manager():
    def __init__(self):
        self.tasks = {}

    def add_task(self,task):
        if task.name not in self.tasks:
            self.tasks[task.name] = task
        else:
            raise Exception('不允许添加相同名字的任务！')

    def run_tasks(self,args=()):
        for task in self.tasks.values():
            task.start(args=args)

    def run_task_by_name(self,name,args=()):
        self.tasks[name].start(args=args)

    def stop_tasks(self):
        for task in self.values():
            task.stop()

    def stop_task_by_name(self,name):
        self.tasks[name].stop()

    def restart_tasks(self):
        for task in self.tasks.values():
            task.restart()

    def restart_task_by_name(self,name):
        self.tasks[name].restart()

    def set_loop_by_name(self,name,unit,interval,start_time):
        self.tasks[name].set_loop(unit, interval, start_time)

    def load_tasks(self):
        task_files = glob(os.path.join(app.config['task_path'],'*.py'))
        print('loading tasks...')
        for file in task_files:
            if '__init__' not in file:
                t = Task(name=file, file=file)
                self.add_task(t)
        print('loading finish')

@app.route("/")
def index():
    now = datetime.datetime.now().strftime('%H:%M:%S')
    return render_template("index.html",tasks=manager.tasks,now=now)

@app.route("/taskinfo/<task_name>")
def task_info(task_name):
    return render_template("task_info.html",task_name=task_name,info=manager.tasks[task_name].all_info)

@app.route("/list_tasks")
def list_tasks():
    # return jsonify({'Access-Control-Allow-Origin': '*','code':200,'data':[task.info for task in manager.tasks]})
    response = make_response({'tasks':[str_dict(task.info) for task in manager.tasks.values()]}, 200)
    # response.headers["Access-Control-Allow-Origin"] = "*" # 这样也能解决跨域问题
    return response

@app.route("/task_allinfo/<task_name>")
def task_allinfo(task_name):
    response = make_response(str_dict(manager.tasks[task_name].all_info), 200)
    return response

@app.route("/addtask",methods=['POST'])
def addtask():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['task_path'], f.filename))
        task = Task(name=os.path.join(app.config['task_path'], f.filename),
                    file=os.path.join(app.config['task_path'], f.filename))
        manager.add_task(task)
        return redirect("/")

# @app.route("/addtask",methods=['GET', 'POST'])
# def add_task():
#     taskpath = request.form.get('taskpath')
#     task = Task(name=taskpath, file=taskpath)
#     manager.add_task(task)
#     return render_template("index.html",taskstatus=manager.task_status())

@app.route("/runtasks",methods=['POST'])
def run_tasks():
    manager.run_tasks()
    return redirect("/")

@app.route("/runtask_by_name/<name>")
def run_task_by_name(name):
    args = []
    manager.run_task_by_name(name=name,args=tuple(args))
    return redirect("/")

@app.route("/stoptasks")
def stop_tasks():
    manager.stop_tasks()
    return redirect("/")

@app.route("/stoptask_by_name/<name>")
def stop_task_by_name(name):
    manager.stop_task_by_name(name)
    return redirect("/")

@app.route("/restarttasks")
def restart_tasks():
    manager.restart_tasks()
    return redirect("/")

@app.route("/restarttask_by_name/<name>")
def restart_task_by_name(name):
    manager.restart_task_by_name(name)
    return redirect("/")

@app.route("/setloop_by_name",methods=['POST'])
def setloop():
    manager.set_loop_by_name(request.form.get('task_name'),request.form.get('unit'),int(request.form.get('interval')),request.form.get('loop_start_time'))
    return redirect("/")


if __name__ == '__main__':
    config = ConfigParser()
    config.read('default_config.conf')
    if config.get('consumer', 'log') == 'on':
        logconsumer = LogConsumer('LogConsumer',logger=app.logger)
        logconsumer.start()
    if config.get('consumer', 'email') == 'on':
        emailconsumer = EmailConsumer('EmailConsumer')
        emailconsumer.start()



    manager = Manager()
    manager.load_tasks()
    app.run(host='0.0.0.0',port=8000)


