from .exceptions import (
    InvalidTaskDueDateException, InvalidTaskStatus, TaskAlreadyDoneException)
from datetime import datetime


def new():
    return []


def create_task(tasks, name, description=None, due_on=None):
    if due_on and type(due_on) != datetime:
        raise InvalidTaskDueDateException()

    task = {
        'task': name,
        'description': description,
        'due_on': due_on,
        'status': 'pending'
    }
    tasks.append(task)


def list_tasks(tasks, status='all'):
    if status not in ('all', 'pending', 'done'):
        raise InvalidTaskStatus()

    task_list = []
    for idx, task in enumerate(tasks, 1):
        # Important:
        due_on = task['due_on'].strftime('%Y-%m-%d %H:%M:%S')

        t = (idx, task['task'], due_on, task['status'])
        if status == 'all' or task['status'] == status:
            task_list.append(t)

    return task_list


def complete_task(tasks, name=None, id=None):
    if not name and not id:
        raise ValueError('Either name or id are required')
    new_tasks = []
    for idx, task in enumerate(tasks, start=1):
        if (name and name == task['task']) or (id and idx == id):
            if task['status'] == 'done':
                raise TaskAlreadyDoneException()
            task = task.copy()
            task['status'] = 'done'
        new_tasks.append(task)
    return new_tasks
