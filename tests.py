import pytest
import todos
from todos.exceptions import (
    InvalidTaskStatus, TaskAlreadyDoneException,
    InvalidTaskDueDateException, TaskDoesntExistException)
from datetime import datetime


def test_create_todos_template():
    tasks = todos.new()
    assert tasks == []


def test_create_new_task_basic():
    tasks = todos.new()
    todos.create_task(tasks, 'Email team updates')

    assert tasks == [{
        'task': 'Email team updates',
        'description': None,
        'due_on': None,
        'status': 'pending'
    }]


def test_create_new_task_with_description():
    tasks = todos.new()

    todos.create_task(
        tasks, 'Email team updates',
        description='Some more details')

    assert tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': None,
        'status': 'pending'
    }]


def test_create_new_task_with_description_and_due_date():
    tasks = todos.new()

    todos.create_task(
        tasks, 'Email team updates',
        description='Some more details',
        due_on=datetime(2018, 3, 1, 9))

    assert tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }]


def test_create_new_task_due_date_string_datetime():
    tasks = todos.new()

    todos.create_task(
        tasks, 'Email team updates',
        description='Some more details',
        due_on='2018-03-01 09:00:00')

    assert tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),  # datetime object automatically added
        'status': 'pending'
    }]


def test_create_new_task_due_date_string_date():
    tasks = todos.new()

    todos.create_task(
        tasks, 'Email team updates',
        description='Some more details',
        due_on='2018-03-01')

    assert tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1),  # datetime object automatically added
        'status': 'pending'
    }]


def test_create_new_task_invalid_due_date():
    # FIXME: Student's task
    """
    If the date passed is invalid it should raise an:
        `InvalidTaskDueDateException`
    """
    tasks = todos.new()

    with pytest.raises(InvalidTaskDueDateException):
        todos.create_task(
            tasks, 'Email team updates',
            description='Some more details',
            due_on='not-a-datetime-object')


def test_create_multiple_tasks():
    tasks = todos.new()

    todos.create_task(
        tasks, 'Email team updates',
        description='Some more details',
        due_on=datetime(2018, 3, 1, 9))

    assert tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }]

    todos.create_task(
        tasks, 'Update project plan',
        description='Important before investors meeting',
        due_on=datetime(2018, 3, 5, 9))

    assert tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 3, 5, 9),
        'status': 'pending'
    }]


def test_list_tasks():
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    task_list = todos.list_tasks(tasks)
    assert task_list == [
        (1, 'Email team updates', '2018-03-01 09:00:00', 'pending'),
        (2, 'Update project plan', '2018-02-28 09:00:00', 'done'),
        (3, 'Book conference room', '2018-03-01 08:30:00', 'pending'),
    ]


def test_list_pending_tasks():
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    task_list = todos.list_tasks(tasks, status='pending')
    assert task_list == [
        (1, 'Email team updates', '2018-03-01 09:00:00', 'pending'),
        (3, 'Book conference room', '2018-03-01 08:30:00', 'pending'),
    ]


def test_list_completed_tasks():
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    task_list = todos.list_tasks(tasks, status='done')
    assert task_list == [
        (2, 'Update project plan', '2018-02-28 09:00:00', 'done'),
    ]


def test_list_invalid_status_task():
    # FIXME: Student's task
    """
    If the `list_tasks` method receives an invalid status, it should raise
    an `InvalidTaskStatus` Exception
    """
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    with pytest.raises(InvalidTaskStatus):
        todos.list_tasks(tasks, status='INVALID TYPE')


def test_complete_task_by_name():
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    new_tasks = todos.complete_task(tasks, 'Email team updates')

    assert new_tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'done'  # Was updated
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    # Original tasks were not changed
    assert tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]


def test_complete_task_by_id():
    # FIXME: Student's task
    """
    The task to complete can be given by either the name, or the order
    within the JSON file (starting from 1).
    """
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    new_tasks = todos.complete_task(tasks, "1")

    assert new_tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'done'  # Was updated
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    # Original tasks were not changed
    assert tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]


def test_complete_task_already_done():
    # FIXME: Student's task
    """
    If the task is already done, it should raise a:
        `TaskAlreadyDoneException`
    """
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    with pytest.raises(TaskAlreadyDoneException):
        todos.complete_task(tasks, 'Update project plan')


def test_complete_task_doesnt_exist_fails():
    # FIXME: Student's task
    """
    If the task doesn't exist (either name or position), it should raise:
        `TaskDoesntExistException`
    """
    tasks = []

    with pytest.raises(TaskDoesntExistException):
        todos.complete_task(tasks, 'DOES NOT EXIST')

    with pytest.raises(TaskDoesntExistException):
        todos.complete_task(tasks, '9')


def test_task_summary():
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    summary = todos.summary(tasks)

    assert summary == {
        'total': 3,
        'pending': 2,
        'done': 1
    }


def test_export_tasks_json_compatible():
    tasks = [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': datetime(2018, 3, 1, 9),
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': datetime(2018, 2, 28, 9),
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': datetime(2018, 3, 1, 8, 30),
        'status': 'pending'
    }]

    json_valid_tasks = todos.serialize(tasks)

    assert json_valid_tasks == [{
        'task': 'Email team updates',
        'description': 'Some more details',
        'due_on': '2018-03-01 09:00:00',
        'status': 'pending'
    }, {
        'task': 'Update project plan',
        'description': 'Important before investors meeting',
        'due_on': '2018-02-28 09:00:00',
        'status': 'done'
    }, {
        'task': 'Book conference room',
        'description': None,
        'due_on': '2018-03-01 08:30:00',
        'status': 'pending'
    }]
