from SpiderAdmin.spideradmin.task import Task
import time
import os
from glob import glob
from flask import Flask, send_file, render_template,request,redirect
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['task_path'] = 'SpiderAdmin/spideradmin/task_code'


class Manager():
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        if task.name not in [task.name for task in self.tasks]:
            self.tasks.append(task)
        else:
            raise Exception('不允许添加相同名字的任务！')

    def run_tasks(self,args=()):
        for task in self.tasks:
            # if task.status != 'running':
            task.start(args=args)

    def run_task_by_name(self,name,args=()):
        for task in self.tasks:
            if task.name == name:
                # if task.status != 'running':
                task.start(args=args)
                break

    def stop_tasks(self):
        for task in self.tasks:
            # if task.status != 'stopped':
            task.stop()

    def stop_task_by_name(self,name):
        for task in self.tasks:
            if task.name == name:
                # if task.status != 'stopped':
                task.stop()
                break

    def restart_tasks(self):
        for task in self.tasks:
            task.restart()

    def restart_task_by_name(self,name):
        for task in self.tasks:
            if task.name == name:
                task.restart()
                break

    def load_tasks(self):
        task_files = glob(os.path.join(app.config['task_path'],'*.py'))
        for file in task_files:
            if '__init__' not in file:
                self.add_task(Task(name=file, file = file))

@app.route("/")
def index():
    return render_template("index.html",tasks=manager.tasks)

@app.route("/taskinfo/<task_name>")
def task_info(task_name):
    for task in manager.tasks:
        if task.name == task_name:
            info = task.all_info
    return render_template("task_info.html",task_name=task_name,info=info)

@app.route("/tasks")
def tasks():
    return manager.tasks()

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

@app.route("/runtask_by_name",methods=['POST'])
def run_task_by_name():
    args = []
    for key in request.form.keys():
        if key != 'task_name':
            args.append(request.form.get(key))
    print(request.form.get('task_name'))
    manager.run_task_by_name(name=request.form.get('task_name'),args=tuple(args))
    return redirect("/")

@app.route("/stoptasks")
def stop_tasks():
    manager.stop_tasks()
    return redirect("/")

@app.route("/stoptask_by_name/<name>")
def stoptask_by_name(name):
    manager.stop_task_by_name(name)
    return redirect("/")

@app.route("/restarttasks")
def restart_tasks():
    manager.restart_tasks()
    return redirect("/")

@app.route("/restarttask_by_name/<name>")
def restarttask_by_name(name):
    manager.restart_task_by_name(name)
    return redirect("/")


if __name__ == '__main__':
    manager = Manager()
    manager.load_tasks()
    app.run(debug=True)
