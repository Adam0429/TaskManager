import threading
from task import Task
import time
import os
import sys

from flask import Flask,jsonify


app = Flask(__name__)


class Manager():
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        if task.name not in [task.name for task in self.tasks]:
            self.tasks.append(task)
        else:
            raise Exception('不允许添加相同名字的任务！')

    def run_task_by_name(self,name):
        for task in self.tasks:
            if task.name == name:
                if task.status != 'running':
                    task.start()
                    break

    def run_tasks(self):
        for task in self.tasks:
            if task.status != 'running':
                task.start()

    def run_task_by_name(self,name):
        for task in self.tasks:
            if task.name == name:
                if task.status != 'stopped':
                    task.stop()
                    break

    def stop_tasks(self):
        for task in self.tasks:
            if task.status != 'stopped':
                task.stop()

    def task_status(self):
        status = {}
        for task in self.tasks:
            status[task.name] = task.status
        return status


def fun1():
    for i in range(100):
        print(i)
        time.sleep(1)


@app.route("/taskstatus")
def status():
    return manager.task_status()

@app.route("/addtask/<name>")
def addtask(name):
    task = Task(name=name, target=fun1)
    manager.add_task(task)
    return 'success'

@app.route("/runtasks")
def runtasks():
    manager.run_tasks()
    return 'success'

@app.route("/runtask_by_name/<name>")
def runtask_by_name(name):
    manager.run_task_by_name(name)
    return 'success'

if __name__ == '__main__':
    manager = Manager()
    app.run(debug=True)
