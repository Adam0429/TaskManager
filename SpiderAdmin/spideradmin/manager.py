from SpiderAdmin.spideradmin.task import Task
import time
import os

from flask import Flask, send_file, render_template,request


app = Flask(__name__)


class Manager():
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        if task.name not in [task.name for task in self.tasks]:
            self.tasks.append(task)
        else:
            raise Exception('不允许添加相同名字的任务！')

    def run_tasks(self):
        for task in self.tasks:
            # if task.status != 'running':
                task.start()

    def run_task_by_name(self,name):
        for task in self.tasks:
            if task.name == name:
                # if task.status != 'running':
                task.start()
                break

    def stop_tasks(self):
        for task in self.tasks:
            if task.status != 'stopped':
                task.stop()
        time.sleep(1)

    def stop_task_by_name(self,name):
        for task in self.tasks:
            if task.name == name:
                if task.status != 'stopped':
                    task.stop()
                    break
        time.sleep(1)

    def restart_tasks(self):
        for task in self.tasks:
            task.restart()

    def restart_task_by_name(self,name):
        for task in self.tasks:
            if task.name == name:
                task.restart()
                break
    
    def task_status(self):
        status = {}
        for task in self.tasks:
            status[task.name] = task.status
        return status


@app.route("/")
def admin_vue():
    return render_template("index.html",taskstatus=manager.task_status())

@app.route("/taskstatus")
def status():
    return manager.task_status()

@app.route("/addtask",methods=['GET', 'POST'])
def add_task():
    taskname = request.form.get('taskname')
    task = Task(name=taskname, target=fun1)
    manager.add_task(task)
    return render_template("index.html",taskstatus=manager.task_status())

@app.route("/runtasks")
def run_tasks():
    manager.run_tasks()
    return render_template("index.html",taskstatus=manager.task_status())

@app.route("/runtask_by_name/<name>")
def run_task_by_name(name):
    manager.run_task_by_name(name)
    return render_template("index.html",taskstatus=manager.task_status())

@app.route("/stoptasks")
def stop_tasks():
    manager.stop_tasks()
    return render_template("index.html",taskstatus=manager.task_status())

@app.route("/stoptask_by_name/<name>")
def stoptask_by_name(name):
    manager.stop_task_by_name(name)
    return render_template("index.html",taskstatus=manager.task_status())

@app.route("/restarttasks")
def restart_tasks():
    manager.restart_tasks()
    return render_template("index.html",taskstatus=manager.task_status())

@app.route("/restarttask_by_name/<name>")
def restarttask_by_name(name):
    manager.restart_task_by_name(name)
    return render_template("index.html",taskstatus=manager.task_status())


def fun1():
    for i in range(100):
        print(i)
        time.sleep(1)

if __name__ == '__main__':
    manager = Manager()
    app.run(debug=True)
