import json
from datetime import datetime
from .exceptions import InvalidTaskDueDateException


def parse_date(date_str):
    formats = [
        '%Y-%m-%d',
        '%Y-%m-%d %H:%M:%S',
    ]
    if date_str is None:
        return date_str
    for format in formats:
        try:
            return datetime.strptime(date_str, format)
        except ValueError:
            pass


def parse_int(value):
    pass


def serialize(tasks):
    new_tasks = []
    for task in tasks:
        task = task.copy()
        task['due_on'] = task['due_on'].strftime('%Y-%m-%d %H:%M:%S')
        new_tasks.append(task)
    return new_tasks


def unserialize(blob):
    raw_tasks = json.loads(blob)
    new_tasks = []
    for task in raw_tasks:
        task = task.copy()
        task['due_on'] = parse_date(task['due_on'])
        new_tasks.append(task)
    return new_tasks


def summary(tasks):
    summary_obj = {
        'total': len(tasks),
        'pending': 0,
        'done': 0,
    }
    for task in tasks:
        if task['status'] == 'pending':
            summary_obj['pending'] += 1

        if task['status'] == 'done':
            summary_obj['done'] += 1

    return summary_obj
